#!/usr/bin/env python3
"""Ingest OpenStates bills into Republic OS legislation files.

The legislative-process corpus, parallel to the LegalText statute corpus:
a bill is a proposed change to law. Each bill node records its version chain
(the diff), action timeline (the PR events), sponsors (authors), and votes
(the merge decisions). Source is the OpenStates/OpenCivicData bulk dump.

Mechanical: raw JSONL export (one bill per line) -> OKF Bill Markdown nodes.
No summaries or interpretation. Deterministic: same input -> byte-identical output.

  scripts/ingest_legislation.py --state fl --input data/legislation/fl.jsonl
"""

import argparse
import hashlib
import json
import re
import shutil
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
OUT_ROOT = REPO / "legislation" / "us" / "states"

RETRIEVED_AT = "2026-07-06"
DEFAULT_VINTAGE = "2026-07-01"


def snapshot_url(vintage):
    return f"https://data.openstates.org/daily/{vintage}/public.pgdump"


# Values that appear in the OpenStates `subject` field but are scraper artifacts,
# not real topic tags (e.g. FL stores the literal link text "Subject Index").
JUNK_SUBJECTS = {"subject index"}

DEPOT_SRC = "/Volumes/depot/exports/legislation"

# Official-name exceptions; the fallback is "{State} Legislature".
LEGISLATURE = {
    "co": "Colorado General Assembly", "ct": "Connecticut General Assembly",
    "de": "Delaware General Assembly", "ga": "Georgia General Assembly",
    "il": "Illinois General Assembly", "in": "Indiana General Assembly",
    "ia": "Iowa General Assembly", "ky": "Kentucky General Assembly",
    "md": "Maryland General Assembly", "mo": "Missouri General Assembly",
    "nc": "North Carolina General Assembly", "oh": "Ohio General Assembly",
    "pa": "Pennsylvania General Assembly", "ri": "Rhode Island General Assembly",
    "sc": "South Carolina General Assembly", "tn": "Tennessee General Assembly",
    "vt": "Vermont General Assembly", "va": "Virginia General Assembly",
    "ma": "Massachusetts General Court", "nh": "New Hampshire General Court",
    "nd": "North Dakota Legislative Assembly", "or": "Oregon Legislative Assembly",
}
STATE_NAME = {
    "al": "Alabama", "ak": "Alaska", "az": "Arizona", "ar": "Arkansas",
    "ca": "California", "co": "Colorado", "ct": "Connecticut", "de": "Delaware",
    "fl": "Florida", "ga": "Georgia", "hi": "Hawaii", "id": "Idaho",
    "il": "Illinois", "in": "Indiana", "ia": "Iowa", "ks": "Kansas",
    "ky": "Kentucky", "la": "Louisiana", "me": "Maine", "md": "Maryland",
    "ma": "Massachusetts", "mi": "Michigan", "mn": "Minnesota", "ms": "Mississippi",
    "mo": "Missouri", "mt": "Montana", "ne": "Nebraska", "nv": "Nevada",
    "nh": "New Hampshire", "nj": "New Jersey", "nm": "New Mexico", "ny": "New York",
    "nc": "North Carolina", "nd": "North Dakota", "oh": "Ohio", "ok": "Oklahoma",
    "or": "Oregon", "pa": "Pennsylvania", "ri": "Rhode Island", "sc": "South Carolina",
    "sd": "South Dakota", "tn": "Tennessee", "tx": "Texas", "ut": "Utah",
    "vt": "Vermont", "va": "Virginia", "wa": "Washington", "wv": "West Virginia",
    "wi": "Wisconsin", "wy": "Wyoming",
}


def yval(value):
    if value is None:
        return '""'
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, int):
        return str(value)
    if isinstance(value, list):
        return "[" + ", ".join(yval(v) for v in value) + "]"
    return json.dumps(str(value), ensure_ascii=False)


def slugify(value):
    value = (value or "").lower()
    value = re.sub(r"[^a-z0-9]+", "-", value).strip("-")
    return re.sub(r"-{2,}", "-", value) or "unnamed"


def sha256_text(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def version_rank(note):
    """Order a bill's versions into a commit chain from its OpenStates note."""
    tok = (note or "").split()[-1].lower() if note else ""
    if tok in ("filed", "introduced", "original"):
        return (0, 0)
    m = re.fullmatch(r"c(\d+)", tok)
    if m:
        return (1, int(m.group(1)))
    m = re.fullmatch(r"e(\d+)", tok)
    if m:
        return (2, int(m.group(1)))
    if tok in ("er", "enrolled"):
        return (3, 0)
    return (1, 50)  # unknown mid-stage: sort stably after filed


STAGE_LABEL = {0: "filed", 1: "committee substitute", 2: "engrossed", 3: "enrolled"}


def clean(s):
    return re.sub(r"\s+", " ", (s or "").strip())


def primary_person_sponsors(sponsors):
    return [clean(s["name"]) for s in sponsors
            if s.get("primary") and s.get("entity_type") == "person"]


def chapter_law(actions):
    for a in actions:
        m = re.search(r"Chapter No\.\s*([0-9][0-9-]*)", a.get("description") or "")
        if m:
            return m.group(1)
    return None


def render_bill(rec, state, vintage):
    ident = clean(rec["identifier"])
    session = clean(rec["session"])
    title = clean(rec.get("title")) or ident
    sponsors = rec.get("sponsors") or []
    actions = rec.get("actions") or []
    versions = sorted(rec.get("versions") or [], key=lambda v: (version_rank(v.get("note")), v.get("note") or ""))
    votes = rec.get("votes") or []
    subjects = [clean(x) for x in (rec.get("subjects") or [])
                if clean(x) and clean(x).lower() not in JUNK_SUBJECTS]
    prim = primary_person_sponsors(sponsors)
    chap = chapter_law(actions)
    dates = [a.get("date") for a in actions if a.get("date")]
    citation = f"{STATE_NAME.get(state, state.upper())} {ident} ({session})"

    fm = {
        "type": "Bill",
        "title": title,
        "description": clean(rec.get("abstract")) or title,
        "jurisdiction": f"us/states/{state}",
        "legislature": LEGISLATURE.get(state, f"{STATE_NAME.get(state, state.upper())} Legislature"),
        "session": session,
        "identifier": ident,
        "citation": citation,
        "classification": rec.get("classification") or [],
        "subjects": subjects,
        "status": "enacted",
        "chapter_law": chap,
        "primary_sponsors": prim,
        "version_count": len(versions),
        "action_count": len(actions),
        "vote_count": len(votes),
        "first_action": min(dates) if dates else None,
        "last_action": max(dates) if dates else None,
        "source": "openstates",
        "source_identifier": rec["bill_id"],
        "source_url": (rec.get("sources") or [None])[0],
        "source_hash": sha256_text(json.dumps(rec, sort_keys=True, ensure_ascii=False)),
        "vintage": vintage,
        "source_snapshot": snapshot_url(vintage),
        "retrieved_at": RETRIEVED_AT,
        "confidence": "reported",
        "tags": ["legislation", "bill", f"us-{state}"],
    }
    # drop null-valued optional keys for clean, deterministic frontmatter
    fm = {k: v for k, v in fm.items() if v is not None}

    out = ["---"]
    for k, v in fm.items():
        out.append(f"{k}: {yval(v)}")
    out.append("---")
    out.append("")
    out.append(f"# {citation} — {title}")
    out.append("")
    if fm["description"] != title:
        out.append(fm["description"])
        out.append("")
    if chap:
        out.append(f"**Enacted** — Laws of {STATE_NAME.get(state, state.upper())}, Chapter {chap}.")
        out.append("")

    out.append("## Version chain")
    out.append("")
    out.append("The bill's text revisions, in order — the diff chain from filing to enrollment.")
    out.append("")
    for i, v in enumerate(versions):
        stage = STAGE_LABEL[version_rank(v.get("note"))[0]]
        note = clean(v.get("note")) or stage
        link = f" — [source]({v['url']})" if v.get("url") else ""
        out.append(f"{i+1}. **{note}** ({stage}){link}")
    out.append("")

    if votes:
        out.append("## Votes")
        out.append("")
        for v in votes:
            y, n = v.get("yes"), v.get("no")
            tally = f"{y}–{n}" if y is not None and n is not None else (v.get("result") or "")
            ch = clean(v.get("chamber")) or ""
            motion = clean(v.get("motion")) or "vote"
            out.append(f"- {motion} — **{tally}** ({v.get('result')}) {('· ' + ch) if ch else ''}".rstrip())
        out.append("")

    if sponsors:
        out.append("## Sponsors")
        out.append("")
        for s in sponsors:
            role = "primary" if s.get("primary") else (clean(s.get("classification")) or "cosponsor")
            out.append(f"- {clean(s['name'])} — {role} ({clean(s.get('entity_type'))})")
        out.append("")

    out.append("## Timeline")
    out.append("")
    out.append("The legislative action history — every referral, reading, and vote.")
    out.append("")
    for a in actions:
        cls = ", ".join(a.get("classification") or [])
        tag = f" `{cls}`" if cls else ""
        out.append(f"- **{a.get('date') or '—'}** {clean(a.get('description'))}{tag}")
    out.append("")

    out.append("## Source")
    out.append("")
    out.append(f"OpenStates / OpenCivicData bulk snapshot [{vintage}]({snapshot_url(vintage)}); "
               f"origin `{rec['bill_id']}`. Confidence: reported (aggregated from official {STATE_NAME.get(state, state.upper())} legislature records).")
    out.append("")

    path = OUT_ROOT / state / slugify(session) / f"{slugify(ident)}.md"
    return path, "\n".join(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--state", required=True)
    ap.add_argument("--input", default=None,
                    help="raw JSONL; default: depot export for --vintage")
    ap.add_argument("--vintage", default=DEFAULT_VINTAGE,
                    help="OpenStates bulk-snapshot date, e.g. 2026-07-01")
    args = ap.parse_args()
    state = args.state.lower()
    src = args.input or f"{DEPOT_SRC}/{args.vintage}/enacted_{state}_{args.vintage}.jsonl"

    dest = OUT_ROOT / state
    if dest.exists():
        shutil.rmtree(dest)

    n = 0
    used = {}
    with open(src, encoding="utf-8") as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            rec = json.loads(line)
            # Record ALL enacted legislation honestly — bills AND joint/concurrent
            # resolutions. The classification frontmatter says which; filtering
            # (e.g. dropping TN's ceremonial resolutions) is a view's job, not the
            # mirror's.
            path, content = render_bill(rec, state, args.vintage)
            occ = used.get(path, 0) + 1
            used[path] = occ
            if occ > 1:
                path = path.with_name(f"{path.stem}-{occ}.md")
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content + "\n", encoding="utf-8")
            n += 1
    print(f"{state}: wrote {n} enacted-legislation nodes to {dest.relative_to(REPO)}")


if __name__ == "__main__":
    main()
