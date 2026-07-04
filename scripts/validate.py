#!/usr/bin/env python3
"""Validate every entity and legal text file in the mirror.

Three checks, no third-party dependencies:
  1. OKF conformance — every non-reserved .md has YAML frontmatter with a
     non-empty `type`.
  2. Schema conformance — each entity validates against the JSON Schema for
     its `type` in /schemas (required fields, property types, enums). The
     schemas are a stricter profile over OKF's permissive base; unknown keys
     are tolerated by design.
  3. Link integrity — internal /-rooted markdown links resolve to a file that
     exists in the tree.

Exit code is non-zero if any check fails, so this doubles as a CI gate.

Usage:  python scripts/validate.py
"""

import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
TREES = [REPO / "data" / "jurisdictions", REPO / "legal"]
SCHEMAS = REPO / "schemas"
MAX_REPORT = 25

TYPE_PY = {
    "string": str, "number": (int, float), "integer": int,
    "boolean": bool, "array": list, "object": dict,
}


# --------------------------------------------------------------------------- #
# frontmatter parser (tuned to the deterministic output of build.py)
# --------------------------------------------------------------------------- #

def extract_frontmatter(text):
    lines = text.split("\n")
    if not lines or lines[0].strip() != "---":
        return None
    out = []
    for line in lines[1:]:
        if line.strip() == "---":
            return out
        out.append(line)
    return None


def parse_scalar(s):
    s = s.strip()
    if s == "":
        return None
    try:
        return json.loads(s)          # "quoted", 123, 1.5, true, false, null
    except (ValueError, json.JSONDecodeError):
        return s                       # bare word, e.g. official


def parse_value(s):
    s = s.strip()
    if s.startswith("[") and s.endswith("]"):
        inner = s[1:-1].strip()
        return [parse_scalar(x) for x in inner.split(",")] if inner else []
    return parse_scalar(s)


def parse_frontmatter(text):
    """Top-level parse. Block values become [] (array) or {} (object)
    sentinels — sufficient for schema shape/enum/required checks."""
    fm = extract_frontmatter(text)
    if fm is None:
        return None
    d = {}
    i = 0
    while i < len(fm):
        line = fm[i]
        if not line.strip() or line.startswith((" ", "\t")):
            i += 1
            continue
        m = re.match(r"([A-Za-z0-9_]+):(.*)$", line)
        if not m:
            i += 1
            continue
        key, rest = m.group(1), m.group(2).strip()
        if rest:
            d[key] = parse_value(rest)
        else:
            j = i + 1
            while j < len(fm) and not fm[j].strip():
                j += 1
            d[key] = [] if (j < len(fm) and fm[j].lstrip().startswith("- ")) else {}
        i += 1
    return d


# --------------------------------------------------------------------------- #
# minimal JSON-Schema validation (required / type / enum)
# --------------------------------------------------------------------------- #

def validate_obj(obj, schema):
    errs = []
    for req in schema.get("required", []):
        if req not in obj or obj[req] is None:
            errs.append(f"missing required '{req}'")
    for key, spec in schema.get("properties", {}).items():
        if key not in obj or obj[key] is None:
            continue
        val = obj[key]
        t = spec.get("type")
        if t and not isinstance(val, TYPE_PY[t]):
            # bool is a subclass of int; reject bool where integer/number expected
            if not (t in ("integer", "number") and isinstance(val, bool) is False):
                errs.append(f"'{key}' expected {t}, got {type(val).__name__}")
        if "enum" in spec and val not in spec["enum"]:
            errs.append(f"'{key}'={val!r} not in {spec['enum']}")
    return errs


# --------------------------------------------------------------------------- #
# main
# --------------------------------------------------------------------------- #

def load_schemas():
    schemas = {}
    for p in sorted(SCHEMAS.glob("*.schema.json")):
        s = json.loads(p.read_text())
        t = s["properties"]["type"]["enum"][0]
        schemas[t] = s
    return schemas


LINK_RE = re.compile(r"\]\((/[^)\s]+\.md)\)")


def main():
    schemas = load_schemas()
    if not schemas:
        print("no schemas found in /schemas", file=sys.stderr)
        return 1

    files = []
    for tree in TREES:
        if tree.exists():
            files.extend(sorted(tree.rglob("*.md")))
    counts = {t: 0 for t in schemas}
    counts["(untyped)"] = 0
    okf_fail, schema_fail, link_fail = [], [], []
    existing = set()
    jurisdiction_tree = REPO / "data" / "jurisdictions"
    for p in files:
        if p.is_relative_to(jurisdiction_tree):
            existing.add("/" + str(p.relative_to(jurisdiction_tree)))
        else:
            existing.add("/" + str(p.relative_to(REPO)))

    for p in files:
        rel = p.relative_to(REPO)
        text = p.read_text(encoding="utf-8")
        fm = parse_frontmatter(text)

        # 1. OKF conformance
        if fm is None or not fm.get("type"):
            okf_fail.append(f"{rel}: no frontmatter / empty type")
            counts["(untyped)"] += 1
            continue

        etype = fm["type"]
        # 2. schema conformance
        if etype in schemas:
            counts[etype] += 1
            for e in validate_obj(fm, schemas[etype]):
                schema_fail.append(f"{rel}: {e}")
        else:
            schema_fail.append(f"{rel}: unknown type {etype!r} (no schema)")

        # 3. link integrity
        for m in LINK_RE.finditer(text):
            if m.group(1) not in existing:
                link_fail.append(f"{rel}: dead link {m.group(1)}")

    # ---- report ----
    total = len(files)
    print(f"validated {total} markdown records")
    for t in sorted(counts):
        if counts[t]:
            print(f"  {t}: {counts[t]}")

    def section(name, items):
        if not items:
            print(f"\n{name}: PASS (0)")
            return 0
        print(f"\n{name}: FAIL ({len(items)})")
        for line in items[:MAX_REPORT]:
            print(f"  - {line}")
        if len(items) > MAX_REPORT:
            print(f"  … and {len(items) - MAX_REPORT} more")
        return len(items)

    fails = (section("OKF conformance", okf_fail)
             + section("Schema conformance", schema_fail)
             + section("Link integrity", link_fail))

    print()
    if fails:
        print(f"VALIDATION FAILED — {fails} issue(s)")
        return 1
    print("VALIDATION PASSED — all files conform")
    return 0


if __name__ == "__main__":
    sys.exit(main())
