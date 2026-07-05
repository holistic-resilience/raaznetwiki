#!/usr/bin/env python3
"""Propose raaznetwiki updates from an upstream privacyguides release.

Given a privacyguides.org release, this:

  1. resolves the release + its predecessor and fetches the markdown diff
     (the GitHub compare view) between the two tags,
  2. builds a compact index of the English wiki (`en/**/*.md` frontmatter),
  3. asks Claude which wiki pages the upstream changes plausibly affect (triage),
  4. asks Claude to draft a concrete edit for each affected page,
  5. writes the revised files into the working tree and emits a PR body,

so a GitHub Action can open a *draft* PR for human review. English only.

Runs in CI (see .github/workflows/upstream-sync.yml) or locally as a dry run:

    RELEASE_TAG=2026.05.07 python scripts/upstream_sync.py
    git diff        # inspect the proposed changes, then `git checkout .` to revert

Env:
  ANTHROPIC_API_KEY  required
  GITHUB_TOKEN       GitHub API auth (optional locally, higher rate limits)
  UPSTREAM_REPO      default "privacyguides/privacyguides.org"
  RELEASE_TAG        release to sync; blank = latest release
  ANTHROPIC_MODEL    default "claude-opus-4-8"
  PR_BODY_PATH       where to write the PR body (default: <scratch>/pr_body.md)
  GITHUB_OUTPUT      workflow outputs file (set by Actions; ignored locally)
"""

import glob
import json
import os
import re
import sys
import urllib.error
import urllib.request

import yaml
import anthropic

UPSTREAM_REPO = os.environ.get("UPSTREAM_REPO", "privacyguides/privacyguides.org")
RELEASE_TAG = os.environ.get("RELEASE_TAG", "").strip()
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")
MODEL = os.environ.get("ANTHROPIC_MODEL", "claude-opus-4-8")
PR_BODY_PATH = os.environ.get("PR_BODY_PATH") or os.path.join(
    os.environ.get("RUNNER_TEMP", "/tmp"), "upstream_sync_body.md"
)

# Keep the upstream diff bounded so the prompt stays a sane size.
MAX_TOTAL_PATCH = 60_000       # chars of upstream patch text total
MAX_SINGLE_PATCH = 15_000      # chars per file before truncation

WIKI_ROOT = "en"
# raaznetwiki's mission — shared, stable prefix for both Claude stages (cached).
MISSION = """\
You maintain the English content of the Raaznet wiki (raaznetwiki), a digital-security
and privacy knowledge base written for people in the Iranian context: activists,
journalists, and privacy-conscious users operating under state surveillance and
censorship. It is a *conceptual* reference — it explains threats, techniques, and
tradeoffs — not a product-recommendation catalog.

You are given changes from privacyguides.org, an upstream privacy project. privacyguides
is a useful signal for what changed in the wider privacy landscape (a tool was
recommended/deprecated, a technique's guidance shifted, a new threat emerged), but it is
a Western, general-audience tool directory. Do NOT copy it verbatim. Only propose a wiki
change when the upstream change reflects something that genuinely matters for the Raaznet
audience and belongs in the affected page. When in doubt, prefer NOT changing content —
false positives waste reviewer time. All output is reviewed by a human before merge."""

log = lambda m: print(m, flush=True)


# --------------------------------------------------------------------------- #
# GitHub API
# --------------------------------------------------------------------------- #

def gh(path):
    url = f"https://api.github.com{path}"
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "raaznet-upstream-sync/1.0",
    }
    if GITHUB_TOKEN:
        headers["Authorization"] = f"Bearer {GITHUB_TOKEN}"
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            return json.loads(resp.read())
    except urllib.error.HTTPError as e:
        raise RuntimeError(f"GitHub API {e.code} for {path}: {e.read().decode()[:300]}")


def resolve_release():
    if RELEASE_TAG:
        rel = gh(f"/repos/{UPSTREAM_REPO}/releases/tags/{RELEASE_TAG}")
    else:
        rel = gh(f"/repos/{UPSTREAM_REPO}/releases/latest")
    return rel["tag_name"], rel.get("body") or ""


def previous_tag(tag, body):
    # Preferred: the "Full Changelog: .../compare/A...B" line in the release body.
    m = re.search(r"/compare/(.+?)\.\.\.(\S+)", body)
    if m and m.group(2).rstrip(")").strip() == tag:
        return m.group(1)
    # Fallback: walk the releases list and take the one published just before `tag`.
    releases = gh(f"/repos/{UPSTREAM_REPO}/releases?per_page=100")
    tags = [r["tag_name"] for r in releases]  # API returns newest-first
    if tag in tags:
        i = tags.index(tag)
        if i + 1 < len(tags):
            return tags[i + 1]
    raise RuntimeError(f"could not determine the release before {tag}")


def upstream_changes(prev, tag):
    """Markdown content files changed between two release tags, with patches."""
    cmp = gh(f"/repos/{UPSTREAM_REPO}/compare/{prev}...{tag}")
    changes, total, dropped = [], 0, []
    for f in cmp.get("files", []):
        name = f["filename"]
        # content markdown only; drop READMEs, includes/, snippets, translations
        if not (name.startswith("docs/") and name.endswith(".md")):
            continue
        if f["status"] not in ("added", "modified"):
            continue
        patch = f.get("patch") or "(no textual diff available — file added or too large)"
        if len(patch) > MAX_SINGLE_PATCH:
            patch = patch[:MAX_SINGLE_PATCH] + "\n… [patch truncated]"
        if total + len(patch) > MAX_TOTAL_PATCH:
            dropped.append(name)
            continue
        total += len(patch)
        changes.append({"file": name, "status": f["status"], "patch": patch})
    if dropped:
        log(f"NOTE: dropped {len(dropped)} upstream file(s) over the patch budget: {dropped}")
    return changes, dropped


# --------------------------------------------------------------------------- #
# Wiki index
# --------------------------------------------------------------------------- #

def parse_frontmatter(path):
    raw = open(path, encoding="utf-8").read()
    fm = {}
    m = re.match(r"^---\n(.*?)\n---\n?", raw, re.DOTALL)
    if m:
        try:
            fm = yaml.safe_load(m.group(1)) or {}
        except yaml.YAMLError:
            fm = {}
    rel = path.replace("\\", "/")
    parts = rel.split("/")
    section = " > ".join(parts[1:-1])
    title = (fm.get("title") or os.path.splitext(parts[-1])[0].replace("_", " ")).strip()
    tags = fm.get("tags") or []
    if not isinstance(tags, list):
        tags = [str(tags)]
    topics = fm.get("topics") or []
    if not isinstance(topics, list):
        topics = [str(topics)]
    return {
        "path": rel,
        "title": title,
        "section": section,
        "tags": [str(t) for t in tags],
        "topics": [str(t) for t in topics],
        "summary": (fm.get("summary") or "").strip(),
    }


def wiki_index():
    files = sorted(glob.glob(f"{WIKI_ROOT}/**/*.md", recursive=True))
    return [parse_frontmatter(f) for f in files]


# --------------------------------------------------------------------------- #
# Claude
# --------------------------------------------------------------------------- #

client = anthropic.Anthropic()


def ask_claude(user_text, schema, max_tokens):
    """One structured-output call. Streams (avoids HTTP timeouts) and returns parsed JSON."""
    system = [{"type": "text", "text": MISSION, "cache_control": {"type": "ephemeral"}}]
    with client.messages.stream(
        model=MODEL,
        max_tokens=max_tokens,
        system=system,
        thinking={"type": "adaptive"},
        output_config={"effort": "high", "format": {"type": "json_schema", "schema": schema}},
        messages=[{"role": "user", "content": user_text}],
    ) as stream:
        msg = stream.get_final_message()
    u = msg.usage
    log(f"    tokens: in={u.input_tokens} out={u.output_tokens} "
        f"cache_read={getattr(u, 'cache_read_input_tokens', 0)}")
    if msg.stop_reason == "refusal":
        raise RuntimeError("Claude refused the request")
    text = next((b.text for b in msg.content if b.type == "text"), None)
    if text is None:
        raise RuntimeError("no text block in Claude response")
    return json.loads(text)


TRIAGE_SCHEMA = {
    "type": "object",
    "additionalProperties": False,
    "properties": {
        "candidates": {
            "type": "array",
            "items": {
                "type": "object",
                "additionalProperties": False,
                "properties": {
                    "wiki_path": {"type": "string"},
                    "upstream_files": {"type": "array", "items": {"type": "string"}},
                    "reason": {"type": "string"},
                    "kind": {"type": "string", "enum": ["update", "new_topic"]},
                },
                "required": ["wiki_path", "upstream_files", "reason", "kind"],
            },
        }
    },
    "required": ["candidates"],
}

EDIT_SCHEMA = {
    "type": "object",
    "additionalProperties": False,
    "properties": {
        "action": {"type": "string", "enum": ["edit", "no_change"]},
        "rationale": {"type": "string"},
        "new_content": {"type": "string"},
    },
    "required": ["action", "rationale", "new_content"],
}


def triage(changes, index):
    user = (
        "UPSTREAM CHANGES (privacyguides release diff):\n"
        f"{json.dumps(changes, indent=2)}\n\n"
        "RAAZNET WIKI PAGES (English; frontmatter index):\n"
        f"{json.dumps(index, indent=2)}\n\n"
        "For each upstream change, decide whether it should prompt an edit to a Raaznet "
        "wiki page. Return `candidates`:\n"
        "  - kind=\"update\": an existing wiki page (set wiki_path to its exact path) that "
        "plausibly needs an edit because of the listed upstream_files.\n"
        "  - kind=\"new_topic\": the upstream change covers something with NO existing wiki "
        "equivalent that is worth a new page (leave wiki_path empty).\n"
        "List at most one candidate per wiki page. Return an empty list if nothing is "
        "relevant to the Raaznet audience. Be conservative."
    )
    return ask_claude(user, TRIAGE_SCHEMA, max_tokens=8000)["candidates"]


def draft_edit(wiki_path, files_for_page, current):
    patches = "\n\n".join(
        f"### {c['file']} ({c['status']})\n```diff\n{c['patch']}\n```" for c in files_for_page
    )
    user = (
        f"Consider whether this Raaznet wiki page needs an edit in light of the upstream "
        f"changes below.\n\nWIKI PAGE `{wiki_path}` (current full content):\n"
        f"-----\n{current}\n-----\n\n"
        f"RELEVANT UPSTREAM CHANGES:\n{patches}\n\n"
        "If the page genuinely warrants an update for the Raaznet audience, set "
        "action=\"edit\" and return the COMPLETE revised file in new_content — make the "
        "smallest change that does the job, preserve the YAML frontmatter and the page's "
        "voice, and do not invent facts. Otherwise set action=\"no_change\" (new_content "
        "empty). Put a one-to-three sentence justification in rationale either way."
    )
    return ask_claude(user, EDIT_SCHEMA, max_tokens=32000)


# --------------------------------------------------------------------------- #
# Outputs
# --------------------------------------------------------------------------- #

def emit_output(key, value):
    gh_out = os.environ.get("GITHUB_OUTPUT")
    if gh_out:
        with open(gh_out, "a", encoding="utf-8") as fh:
            fh.write(f"{key}={value}\n")
    else:
        log(f"OUTPUT {key}={value}")


def build_pr_body(tag, prev, edits, new_topics, dropped):
    lines = [
        f"Automated review of upstream **privacyguides.org** release "
        f"[`{tag}`](https://github.com/{UPSTREAM_REPO}/releases/tag/{tag}) against the "
        f"English wiki.",
        "",
        f"Compared [`{prev}...{tag}`](https://github.com/{UPSTREAM_REPO}/compare/{prev}...{tag}).",
        "",
        "⚠️ **Draft — every proposed edit is a suggestion for a human to review, adjust, or discard.**",
        "",
        "## Proposed edits",
        "",
    ]
    if edits:
        lines += ["| Wiki page | Why (from upstream) |", "| --- | --- |"]
        for e in edits:
            reason = e["rationale"].replace("\n", " ").replace("|", "\\|")
            lines.append(f"| `{e['wiki_path']}` | {reason} |")
    else:
        lines.append("_No page edits proposed._")
    lines += ["", "## New topics not yet covered", ""]
    if new_topics:
        for n in new_topics:
            reason = n["reason"].replace("\n", " ")
            lines.append(f"- {reason} (upstream: {', '.join(n['upstream_files'])})")
    else:
        lines.append("_None._")
    if dropped:
        lines += ["", "## Upstream files not reviewed (over size budget)", ""]
        lines += [f"- `{d}`" for d in dropped]
    lines += ["", "---", "", "🤖 Generated by `.github/workflows/upstream-sync.yml`."]
    return "\n".join(lines) + "\n"


# --------------------------------------------------------------------------- #

def main():
    tag, body = resolve_release()
    prev = previous_tag(tag, body)
    log(f"Syncing {UPSTREAM_REPO} {prev} -> {tag}")

    changes, dropped = upstream_changes(prev, tag)
    log(f"{len(changes)} upstream markdown content file(s) changed")
    if not changes:
        log("No upstream content changes to review.")
        emit_output("has_changes", "false")
        return

    index = wiki_index()
    log(f"{len(index)} English wiki pages indexed")

    log("Triaging…")
    candidates = triage(changes, index)
    updates = [c for c in candidates if c["kind"] == "update" and c["wiki_path"]]
    new_topics = [c for c in candidates if c["kind"] == "new_topic"]
    log(f"{len(updates)} candidate page(s) to review, {len(new_topics)} new-topic suggestion(s)")

    changes_by_file = {c["file"]: c for c in changes}
    valid_paths = {i["path"] for i in index}
    edits = []
    for cand in updates:
        wp = cand["wiki_path"]
        # Guard: only ever touch real files under en/.
        if wp not in valid_paths or not wp.startswith(f"{WIKI_ROOT}/"):
            log(f"  skip {wp}: not an existing en/ page")
            continue
        files_for_page = [changes_by_file[f] for f in cand["upstream_files"] if f in changes_by_file]
        if not files_for_page:
            continue
        log(f"  drafting edit for {wp}…")
        current = open(wp, encoding="utf-8").read()
        result = draft_edit(wp, files_for_page, current)
        if result["action"] != "edit" or not result["new_content"].strip():
            log(f"    no change: {result['rationale']}")
            continue
        with open(wp, "w", encoding="utf-8") as fh:
            fh.write(result["new_content"])
        edits.append({"wiki_path": wp, "rationale": result["rationale"]})
        log(f"    proposed edit written")

    os.makedirs(os.path.dirname(PR_BODY_PATH) or ".", exist_ok=True)
    with open(PR_BODY_PATH, "w", encoding="utf-8") as fh:
        fh.write(build_pr_body(tag, prev, edits, new_topics, dropped))

    emit_output("has_changes", "true" if edits else "false")
    emit_output("pr_title", f"Upstream sync: privacyguides {tag}")
    emit_output("branch", f"upstream-sync/pg-{tag}")
    emit_output("body_path", PR_BODY_PATH)
    log(f"Done. {len(edits)} file(s) edited. PR body at {PR_BODY_PATH}")


if __name__ == "__main__":
    main()
