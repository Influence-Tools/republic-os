#!/usr/bin/env python3
"""Turn a git diff of the entity tree into a human-readable civic changelog.

The diff is the product. Every sync that changes the mirror leaves a git
diff; this reads that diff and says, in plain language, what changed in the
government — added, modified, and removed entities, grouped by type and by
jurisdiction.

Usage:
  python scripts/generate_changelog.py [BASE] [HEAD]      # default HEAD~1..HEAD
  python scripts/generate_changelog.py <BASE> <HEAD> --write   # prepend CHANGELOG.md

With no data changes between the refs, it says so. On an initial load every
entity is an addition; on a re-sync of the same source, only real government
changes surface — which is the point.
"""

import re
import subprocess
import sys
from collections import defaultdict

PREFIX = "data/jurisdictions/"

# Lines that are pure build bookkeeping, not government facts. A file whose only
# change is one of these (the dataset-vintage stamp) did NOT change as a mirror
# of government — it was just re-exported — so it must not surface as a "change".
# See build.py: the frontmatter `timestamp` and the "Generated from ..." footer.
BOOKKEEPING = re.compile(
    r'^\s*timestamp:\s*".*"\s*$'
    r'|^Generated from the Atlas officeholders v\d+ export \(.*\)\.\s*$')


def git(*args):
    return subprocess.run(["git", *args], capture_output=True, text=True,
                          check=True).stdout


def bookkeeping_only_files(base, head):
    """Paths modified ONLY in bookkeeping lines (vintage stamp), to be ignored."""
    diff = git("diff", "--unified=0", f"{base}..{head}", "--", PREFIX)
    changed = defaultdict(list)   # path -> list of changed content lines
    path = None
    for line in diff.splitlines():
        if line.startswith("+++ b/"):
            path = line[6:]
        elif line.startswith("--- ") or line.startswith("diff ") \
                or line.startswith("@@") or line.startswith("index "):
            continue
        elif path and line and line[0] in "+-":
            changed[path].append(line[1:])
    return {p for p, lines in changed.items()
            if lines and all(BOOKKEEPING.match(ln) for ln in lines)}


def classify(path):
    """(entity type, jurisdiction label) from a repo path — fast, no file reads."""
    if not path.startswith(PREFIX):
        return None, None
    rel = path[len(PREFIX):]
    # jurisdiction label
    m = re.match(r"us/states/([a-z]{2})/", rel)
    juris = m.group(1).upper() if m else ("US (federal)" if rel.startswith("us/") else "?")
    # entity type
    if "/candidates/" in rel:
        etype = "Candidate"
    elif "/bodies/" in rel:
        etype = "Body"
    elif rel.endswith("/index.md") or "/districts/" in rel:
        etype = "Jurisdiction"
    elif "/people/" in rel:
        etype = "Person"
    else:
        etype = "Other"
    return etype, juris


PLURAL = {"Person": "people", "Body": "bodies", "Candidate": "candidates",
          "Jurisdiction": "jurisdictions", "Other": "files"}


def pluralize(etype, n):
    return PLURAL.get(etype, etype.lower() + "s") if n != 1 else etype.lower()


def nice_body(path):
    """A readable name for a body file, derived from its path."""
    slug = path.rsplit("/", 1)[-1][:-3]
    kind = "subcommittee" if "/subcommittees/" in path else \
           "committee" if "/committees/" in path else "chamber"
    m = re.search(r"us/bodies/([a-z]+)/", path)
    chamber = m.group(1).title() + " " if m and kind != "chamber" else ""
    return f"{chamber}{slug.replace('-', ' ').title()} ({kind})"


def main():
    argv = [a for a in sys.argv[1:] if not a.startswith("--")]
    write = "--write" in sys.argv
    base = argv[0] if len(argv) > 0 else "HEAD~1"
    head = argv[1] if len(argv) > 1 else "HEAD"

    status = git("diff", "--name-status", f"{base}..{head}", "--", PREFIX)
    date = git("show", "-s", "--format=%cs", head).strip()
    short = git("rev-parse", "--short", base).strip() + ".." + \
        git("rev-parse", "--short", head).strip()

    # tallies[etype][op] = count ; per_state[state][op] = count
    tallies = defaultdict(lambda: defaultdict(int))
    per_state = defaultdict(lambda: defaultdict(int))
    added_bodies = []
    added_by_state = defaultdict(lambda: defaultdict(int))  # state -> etype -> n added
    ignore = bookkeeping_only_files(base, head)
    skipped = 0

    for line in status.splitlines():
        parts = line.split("\t")
        code = parts[0][0]                      # A / M / D / R
        path = parts[-1]                        # new path for renames
        op = {"A": "added", "M": "modified", "D": "removed", "R": "modified"}.get(code)
        if not op:
            continue
        if op == "modified" and path in ignore:
            skipped += 1
            continue
        etype, juris = classify(path)
        if etype is None:
            continue
        tallies[etype][op] += 1
        per_state[juris][op] += 1
        if op == "added":
            added_by_state[juris][etype] += 1
            if etype == "Body":
                added_bodies.append(nice_body(path))

    total = sum(sum(v.values()) for v in tallies.values())

    out = []
    out.append(f"# Government Changelog — {date}")
    out.append("")
    out.append(f"*Diff `{short}` over the mirror.*")
    out.append("")
    if total == 0:
        out.append("No entity changes in this range — the government, as mirrored, held still.")
        if skipped:
            out.append("")
            out.append(f"*({skipped} files were re-exported with a new vintage stamp "
                       f"but no government change.)*")
        emit(out, write)
        return 0

    # summary line
    def phrase(t):
        d = tallies[t]
        bits = [f"+{d['added']}" if d["added"] else "",
                f"~{d['modified']}" if d["modified"] else "",
                f"−{d['removed']}" if d["removed"] else ""]
        return " ".join(b for b in bits if b)

    out.append("## Summary")
    out.append("")
    for t in ("Person", "Body", "Candidate", "Jurisdiction", "Other"):
        if t in tallies:
            out.append(f"- **{t}**: {phrase(t)}")
    out.append("")

    # bodies get named — they are few and load-bearing
    if added_bodies:
        out.append("## New bodies")
        out.append("")
        for b in sorted(added_bodies)[:40]:
            out.append(f"- {b}")
        if len(added_bodies) > 40:
            out.append(f"- … and {len(added_bodies) - 40} more")
        out.append("")

    # jurisdiction rollup
    out.append("## By jurisdiction")
    out.append("")
    for juris in sorted(per_state, key=lambda s: (-sum(per_state[s].values()), s)):
        d = per_state[juris]
        bits = [f"+{d['added']}" if d["added"] else "",
                f"~{d['modified']}" if d["modified"] else "",
                f"−{d['removed']}" if d["removed"] else ""]
        detail = added_by_state.get(juris)
        types = ""
        if detail:
            types = " (" + ", ".join(f"{n} {pluralize(t, n)}"
                                     for t, n in sorted(detail.items())) + ")"
        out.append(f"- **{juris}**: {' '.join(b for b in bits if b)}{types}")
    out.append("")
    out.append(f"*{total} entity changes total.*")
    if skipped:
        out.append("")
        out.append(f"*(Ignored {skipped} files whose only change was the "
                   f"dataset-vintage stamp — re-export, not a government change.)*")

    emit(out, write)
    return 0


def emit(lines, write):
    text = "\n".join(lines) + "\n"
    print(text)
    if write:
        from pathlib import Path
        cl = Path(__file__).resolve().parent.parent / "CHANGELOG.md"
        prev = cl.read_text() if cl.exists() else ""
        cl.write_text(text + "\n---\n\n" + prev)


if __name__ == "__main__":
    sys.exit(main())
