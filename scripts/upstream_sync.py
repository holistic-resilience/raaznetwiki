#!/usr/bin/env python3
"""Propose raaznetwiki updates from an upstream privacyguides release.

Given a privacyguides.org release, this:

  1. resolves the release + its predecessor and fetches the markdown diff
     (the GitHub compare view) between the two tags,
  2. builds a compact index of the English wiki (`en/**/*.md` frontmatter),
  3. asks an LLM which wiki pages the upstream changes plausibly affect (triage),
  4. asks the LLM to draft a concrete edit for each affected page,
  5. writes the revised files into the working tree and emits a PR body,

so a GitHub Action can open a *draft* PR for human review. English only.

The LLM is called through OpenRouter (any OpenAI-compatible model), so the only
credential is an org-owned OpenRouter key — no per-vendor SDK, no personal key.

Runs in CI (see .github/workflows/upstream-sync.yml) or locally as a dry run:

    RELEASE_TAG=2026.05.07 python scripts/upstream_sync.py
    git diff        # inspect the proposed changes, then `git checkout .` to revert

Env:
  OPENROUTER_API_KEY  required (org-owned key)
  OPENROUTER_MODEL    default "google/gemini-2.5-flash"
  GITHUB_TOKEN        GitHub API auth (optional locally, higher rate limits)
  UPSTREAM_REPO       default "privacyguides/privacyguides.org"
  RELEASE_TAG         release to sync; blank = latest release
  PR_BODY_PATH        where to write the PR body (default: <scratch>/pr_body.md)
  GITHUB_OUTPUT       workflow outputs file (set by Actions; ignored locally)
"""

import glob
import json
import os
import re
import urllib.error
import urllib.request

import yaml

UPSTREAM_REPO = os.environ.get("UPSTREAM_REPO", "privacyguides/privacyguides.org")
RELEASE_TAG = os.environ.get("RELEASE_TAG", "").strip()
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")
OPENROUTER_API_KEY = os.environ["OPENROUTER_API_KEY"]
OPENROUTER_MODEL = os.environ.get("OPENROUTER_MODEL", "google/gemini-2.5-flash")
OPENROUTER_URL = "https://openrouter.ai/api/v1/chat/completions"
PR_BODY_PATH = os.environ.get("PR_BODY_PATH") or os.path.join(
    os.environ.get("RUNNER_TEMP", "/tmp"), "upstream_sync_body.md"
)

# Keep the upstream diff bounded so the prompt stays a sane size.
MAX_TOTAL_PATCH = 60_000       # chars of upstream patch text total
MAX_SINGLE_PATCH = 15_000      # chars per file before truncation

WIKI_ROOT = "en"
# raaznetwiki's mission — shared, stable prefix for both LLM stages.
MISSION = """\
You maintain the English content of the Raaznet wiki (raaznetwiki), a digital-security
and privacy knowledge base written for people in the Iranian context: activists,
journalists, and privacy-conscious users operating under state surveillance and
censorship. It is a *conceptual* reference — it explains threats, techniques, and
tradeoffs — not a product-recommendation catalog.

You are given changes from privacyguides.org, an upstream privacy project. privacyguides
is a useful signal for what changed in the wider privacy landscape (a tool was
recommended/deprecated, a technique's guidance shifted, a new threat emerged), but it is
a Western, general-audience tool directory. Do NOT copy it verbatim.

Ground every proposal STRICTLY in facts contained in the provided upstream diff. Do not
introduce information from your own knowledge, and do not propose a change the diff itself
does not support — even if you believe it is true. Only propose a wiki change when the
upstream diff reflects something that genuinely matters for the Raaznet audience and
belongs in the affected page. When in doubt, prefer NOT changing content — false positives
waste reviewer time. All output is reviewed by a human before merge."""

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
# LLM (OpenRouter, OpenAI-compatible)
# --------------------------------------------------------------------------- #

def _extract_json(text):
    """Tolerant JSON extraction — strips code fences / surrounding prose."""
    text = text.strip()
    text = re.sub(r"^```(?:json)?\s*|\s*```$", "", text, flags=re.MULTILINE).strip()
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass
    start, end = text.find("{"), text.rfind("}")
    if start != -1 and end != -1 and end > start:
        return json.loads(text[start:end + 1])
    raise ValueError("no JSON object found in model output")


def ask_llm(user_text, schema, max_tokens):
    """One structured call via OpenRouter. Returns parsed JSON (json_object mode)."""
    system = (
        MISSION
        + "\n\nRespond with a SINGLE JSON object conforming to this JSON schema "
        "(no markdown, no commentary):\n" + json.dumps(schema)
    )
    body = {
        "model": OPENROUTER_MODEL,
        "messages": [
            {"role": "system", "content": system},
            {"role": "user", "content": user_text},
        ],
        "response_format": {"type": "json_object"},
        "temperature": 0,
        "max_tokens": max_tokens,
    }
    for attempt in range(2):
        req = urllib.request.Request(
            OPENROUTER_URL,
            data=json.dumps(body).encode(),
            headers={
                "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                "Content-Type": "application/json",
                "X-Title": "raaznet-upstream-sync",
            },
            method="POST",
        )
        try:
            with urllib.request.urlopen(req, timeout=300) as resp:
                data = json.loads(resp.read())
        except urllib.error.HTTPError as e:
            raise RuntimeError(f"OpenRouter {e.code}: {e.read().decode()[:300]}")
        u = data.get("usage") or {}
        log(f"    tokens: in={u.get('prompt_tokens')} out={u.get('completion_tokens')} "
            f"model={data.get('model')}")
        content = data["choices"][0]["message"]["content"]
        try:
            return _extract_json(content)
        except (ValueError, json.JSONDecodeError):
            if attempt == 0:
                body["messages"] += [
                    {"role": "assistant", "content": content},
                    {"role": "user", "content": "That was not valid JSON. Reply with ONLY the JSON object."},
                ]
                continue
            raise RuntimeError("model did not return valid JSON after retry")


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
        "edits": {
            "type": "array",
            "items": {
                "type": "object",
                "additionalProperties": False,
                "properties": {
                    "old_string": {"type": "string"},
                    "new_string": {"type": "string"},
                },
                "required": ["old_string", "new_string"],
            },
        },
    },
    "required": ["action", "rationale", "edits"],
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
    return ask_llm(user, TRIAGE_SCHEMA, max_tokens=4000)["candidates"]


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
        "action=\"edit\" and return a list of surgical `edits`, each a find/replace pair:\n"
        "  - `old_string`: copied VERBATIM from the page above (exact characters, "
        "whitespace, and punctuation) and long enough to occur exactly once.\n"
        "  - `new_string`: the replacement.\n"
        "Change ONLY what the update requires — do not reflow, re-indent, or reformat any "
        "surrounding text, and do not touch the YAML frontmatter unless the change is to a "
        "frontmatter field. Keep the page's voice; do not invent facts. If nothing warrants "
        "changing, set action=\"no_change\" with an empty `edits` list. Put a one-to-three "
        "sentence justification in rationale either way."
    )
    return ask_llm(user, EDIT_SCHEMA, max_tokens=4000)


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
            if e.get("skipped"):
                reason += f" _({e['skipped']} suggested edit(s) could not be auto-applied)_"
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
    log(f"Syncing {UPSTREAM_REPO} {prev} -> {tag}  (model: {OPENROUTER_MODEL})")

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
        proposed = result.get("edits") or []
        if result["action"] != "edit" or not proposed:
            log(f"    no change: {result['rationale']}")
            continue
        # Apply each find/replace deterministically; require a unique match so we can
        # never corrupt untouched text (a bad/paraphrased old_string is skipped, not forced).
        updated, applied, skipped = current, 0, 0
        for ed in proposed:
            old, new = ed.get("old_string", ""), ed.get("new_string", "")
            if old and updated.count(old) == 1:
                updated = updated.replace(old, new, 1)
                applied += 1
            else:
                skipped += 1
                why = "not found" if not old or updated.count(old) == 0 else "not unique"
                log(f"    skip one edit: old_string {why}")
        if applied == 0:
            log(f"    no applicable edits (all {skipped} skipped)")
            continue
        with open(wp, "w", encoding="utf-8") as fh:
            fh.write(updated)
        edits.append({"wiki_path": wp, "rationale": result["rationale"],
                      "applied": applied, "skipped": skipped})
        log(f"    applied {applied} edit(s)" + (f", skipped {skipped}" if skipped else ""))

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
