# Republic OS

An open, version-controlled mirror of public power in the United States.

Government is already software: statutes are code, agencies are processes, elections change the maintainers, and a bill is a pull request against the law. What government has never had is a **changelog**. This repository is that changelog.

**The diff is the product.** Every file here mirrors the observable public state of a government entity or legal text as a deterministic, sourced, human-readable record. When government changes, the files change, and git makes the change visible, permanent, and inspectable.

## What's in here today

19,721 markdown records, every one schema-validated:

| Entity | Count | What it is |
|---|---:|---|
| **Person** | 13,329 | Current officeholders — federal, all 50 state legislatures, and Florida down to the municipal level. Federal members carry their bioguide ID, leadership roles, and committee seats. |
| **Body** | 233 | The institutions themselves — the U.S. House, the Senate, 49 committees, 181 subcommittees, each with its leadership. |
| **Candidate** | 2,494 | Everyone running for federal office in 2026, from FEC filings. |
| **Jurisdiction** | 3,494 | Every U.S. county (3,131) and 363 congressional districts, each carrying Census demographics — the nationwide skeleton, filled with data. |
| **LegalText** | 171 | U.S. Code Title 52, Voting and Elections, mirrored from the official OLRC XML release current through Public Law 119-100. |

The mirror answers, with receipts: *who holds power, who runs the institution, who's running, what each place is made of,* and now *what legal text governs elections* — and, through git, *what changed.*

## How it works

```
raw source exports         deterministic build          validated tree
data/*.jsonl        ──►    scripts/build.py      ──►    data/jurisdictions/**
data/legal/raw      ──►    scripts/ingest_*.py   ──►    legal/**
(committed as-is)          (one pass)                   (OKF markdown + YAML)
```

- **Format** — Markdown with YAML frontmatter, [OKF](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md)-conformant, validated by JSON Schema in [`/schemas`](schemas). Human-readable in any editor or on GitHub; machine-readable by any agent.
- **Deterministic** — `make build` and `make legal-us-code` regenerate their trees from committed raw sources and pinned official snapshots. Records change only when government changes, so every diff is signal.
- **Sourced** — every record carries field-level provenance and a confidence level. This repo is a *mirror*, never the authority; official sources remain the source of truth.
- **Raw-first** — source exports land in `data/*.jsonl` untouched before any transformation, so the origin is always recoverable.

## Commands

```bash
make build         # regenerate the entity tree from the raw exports
make legal-us-code # regenerate the U.S. Code Title 52 legal corpus seed
make validate      # OKF + schema + link-integrity checks on all records
make changelog     # what changed in the government since the last commit
make board         # rebuild the Board's inlined data from the tree
make check         # build, then validate — the full gate
```

Everything runs on the Python standard library. No dependencies to install.

## Documentation

- [Government as Code](docs/government-as-code.md) — the philosophy: why git, and what its primitives mean for government
- [Data Model](docs/data-model.md) — entity types, IDs, the file format, the jurisdiction tree
- [Sources](docs/sources.md) — where every fact comes from, and how current it is
- [Legal Corpus](docs/legal-corpus.md) — deterministic legal text mirroring, raw snapshots, manifests, and checksums
- [The Board](docs/board.md) — the county map view, how its data is rebuilt, and how to redeploy the Artifact
- [Roadmap](docs/roadmap.md) — what exists, what's next
- [Contributing](docs/contributing.md) — the disciplines, and how to add a source
- [Technical Brief — Government as Software](Technical%20Brief%20—%20Government%20as%20Software.md) — the founding document
- [CHANGELOG.md](CHANGELOG.md) — the civic changelog, generated from git history

## The disciplines

Three rules govern everything here, and they are won by subtraction:

1. **Never overwrite** — a change is a new commit, not a clobbered file. Deletes are diffs.
2. **Never rewrite history** — no force-push, no squash. The past is load-bearing.
3. **Always push off-box** — one copy is a single point of failure; more is not.

Substrate for [influence.tools](https://influence.tools).
