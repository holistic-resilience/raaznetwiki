#!/usr/bin/env python3
"""Index the Raaznet wiki into Qdrant (raaznet_wiki collection).

Runs in CI on content changes. Produces the FLAT payload contract every consumer
depends on (the n8n wiki-search webhook and the Raaznet Telegram bot):

    text, title, section, path, lang, tags, chunk_index   (+ summary, + build_id)

Strategy: embed every chunk (OpenAI text-embedding-3-small, 1536-d, Cosine), upsert
with a per-run build_id, then prune points whose build_id != this run — guarded so a
partial run can never wipe the collection.
"""

import os
import re
import sys
import time
import uuid
import json
import glob
import urllib.request
import urllib.error

import yaml

OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
QDRANT_URL = os.environ["QDRANT_URL"].rstrip("/")
QDRANT_API_KEY = os.environ["QDRANT_API_KEY"]

COLLECTION = "raaznet_wiki"
EMBED_MODEL = "text-embedding-3-small"
VECTOR_SIZE = 1536
CHUNK_SIZE = 1500
CHUNK_OVERLAP = 200
EMBED_BATCH = 96
UPSERT_BATCH = 128
PRUNE_MIN_POINTS = 1000  # never prune if we upserted fewer than this (partial-run guard)

BUILD_ID = str(os.environ.get("GITHUB_RUN_ID") or int(time.time()))
_NS = uuid.uuid5(uuid.NAMESPACE_URL, "raaznet_wiki")


def log(msg):
    print(msg, flush=True)


# --- HTTP helpers ---

def _req(method, url, headers, body=None, timeout=120):
    data = json.dumps(body).encode() if body is not None else None
    r = urllib.request.Request(url, data=data, method=method, headers=headers)
    try:
        with urllib.request.urlopen(r, timeout=timeout) as resp:
            raw = resp.read()
            return resp.status, (json.loads(raw) if raw else {})
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode()[:500]


def qdrant(method, path, body=None):
    return _req(method, f"{QDRANT_URL}{path}",
                {"api-key": QDRANT_API_KEY, "Content-Type": "application/json"}, body)


def embed(texts):
    st, resp = _req("POST", "https://api.openai.com/v1/embeddings",
                    {"Authorization": f"Bearer {OPENAI_API_KEY}", "Content-Type": "application/json"},
                    {"input": texts, "model": EMBED_MODEL})
    if st != 200:
        raise RuntimeError(f"OpenAI embeddings failed ({st}): {resp}")
    return [d["embedding"] for d in resp["data"]]


# --- Parsing + chunking ---

def parse_file(path, root):
    raw = open(path, encoding="utf-8").read()
    fm, body = {}, raw
    m = re.match(r"^---\n(.*?)\n---\n?(.*)$", raw, re.DOTALL)
    if m:
        try:
            fm = yaml.safe_load(m.group(1)) or {}
        except yaml.YAMLError:
            fm = {}
        body = m.group(2)
    rel = os.path.relpath(path, root).replace("\\", "/")
    parts = rel.split("/")
    lang = parts[0] if parts[0] in ("en", "fa") else "en"
    section = " > ".join(parts[1:-1])
    title = (fm.get("title") or os.path.splitext(parts[-1])[0].replace("_", " ")).strip()
    tags = fm.get("tags") or []
    if not isinstance(tags, list):
        tags = [str(tags)]
    summary = (fm.get("summary") or "").strip()
    return {"path": rel, "lang": lang, "section": section, "title": title,
            "tags": [str(t) for t in tags], "summary": summary, "body": body.strip()}


def chunk(body):
    paras = re.split(r"\n{2,}", body)
    chunks, cur = [], ""
    for p in paras:
        if len(cur) + len(p) < CHUNK_SIZE:
            cur = f"{cur}\n\n{p}" if cur else p
        else:
            if cur:
                chunks.append(cur.strip())
            if len(p) > CHUNK_SIZE:
                cur = ""
                for s in re.split(r"(?<=[.!?])\s+", p):
                    if len(cur) + len(s) < CHUNK_SIZE:
                        cur = f"{cur} {s}" if cur else s
                    else:
                        if cur:
                            chunks.append(cur.strip())
                        cur = s
            else:
                cur = p
    if cur.strip():
        chunks.append(cur.strip())
    out = []
    for i, c in enumerate(chunks):
        if i > 0 and len(chunks[i - 1]) > CHUNK_OVERLAP:
            c = chunks[i - 1][-CHUNK_OVERLAP:] + " " + c
        out.append(c)
    return out


# --- Qdrant setup ---

def ensure_collection():
    st, _ = qdrant("GET", f"/collections/{COLLECTION}")
    if st == 404:
        log(f"Creating collection {COLLECTION}")
        st, resp = qdrant("PUT", f"/collections/{COLLECTION}",
                          {"vectors": {"size": VECTOR_SIZE, "distance": "Cosine"}})
        if st not in (200, 201):
            raise RuntimeError(f"create collection failed ({st}): {resp}")
    elif st != 200:
        raise RuntimeError(f"collection check failed ({st})")
    # payload indexes (idempotent) — needed for lang filtering + build_id prune
    for field in ("build_id", "lang"):
        qdrant("PUT", f"/collections/{COLLECTION}/index?wait=true",
               {"field_name": field, "field_schema": "keyword"})


def main():
    root = os.getcwd()
    files = sorted(glob.glob("en/**/*.md", recursive=True) + glob.glob("fa/**/*.md", recursive=True))
    if not files:
        log("No wiki markdown found — refusing to run (would wipe the collection).")
        sys.exit(1)
    log(f"Found {len(files)} markdown files")

    ensure_collection()

    points, upserted = [], 0

    def flush():
        nonlocal points, upserted
        if not points:
            return
        vectors = embed([p["_text"] for p in points])
        body = {"points": [
            {"id": p["id"], "vector": v,
             "payload": {k: val for k, val in p.items() if k not in ("id", "_text")}}
            for p, v in zip(points, vectors)
        ]}
        st, resp = qdrant("PUT", f"/collections/{COLLECTION}/points?wait=true", body)
        if st not in (200, 201):
            raise RuntimeError(f"upsert failed ({st}): {resp}")
        upserted += len(points)
        log(f"  upserted {upserted} points")
        points = []

    for f in files:
        doc = parse_file(f, root)
        for i, ch in enumerate(chunk(doc["body"])):
            points.append({
                "id": str(uuid.uuid5(_NS, f"{doc['path']}#{i}")),
                "_text": ch,
                "text": ch,
                "title": doc["title"],
                "section": doc["section"],
                "path": doc["path"],
                "lang": doc["lang"],
                "tags": doc["tags"],
                "summary": doc["summary"],
                "chunk_index": i,
                "build_id": BUILD_ID,
            })
            if len(points) >= EMBED_BATCH:
                flush()
    flush()

    log(f"Total upserted: {upserted} (build_id={BUILD_ID})")

    # Prune stale points (from removed files / previous builds) — guarded.
    if upserted < PRUNE_MIN_POINTS:
        log(f"Upserted {upserted} < {PRUNE_MIN_POINTS}; SKIPPING prune (partial-run guard).")
        return
    st, resp = qdrant("POST", f"/collections/{COLLECTION}/points/delete?wait=true",
                      {"filter": {"must_not": [{"key": "build_id", "match": {"value": BUILD_ID}}]}})
    if st not in (200, 201):
        raise RuntimeError(f"prune failed ({st}): {resp}")
    log("Pruned stale points from previous builds.")

    st, info = qdrant("GET", f"/collections/{COLLECTION}")
    if st == 200:
        log(f"Done. points_count={info['result'].get('points_count')}")


if __name__ == "__main__":
    main()
