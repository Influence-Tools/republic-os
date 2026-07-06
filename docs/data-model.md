# Data Model

## The file

Every entity is one Markdown file with YAML frontmatter. The frontmatter is the machine-readable record; the body is the human-readable page. The same file serves a journalist reading it on GitHub, an editor in an Obsidian vault, and an AI agent parsing frontmatter.

```markdown
---
type: Person
title: "Mike Johnson"
role: "U.S. House of Representatives - LA-4"
party: "R"
level: "federal"
branch: "legislative"
state: "LA"
leadership:
  - role: "Speaker of the House"
    body: "H"
    since: "2025-01-03"
ids:
  person: "fac58269-6f4a-4706-8eb4-95a549c07a41"
  bioguide: "J000299"
sources:
  - field: tenure
    source: "House Clerk XML 2026-06-10"
  - field: roles
    source: "congress-legislators (unitedstates project)"
confidence: official
tags: [officeholder, federal, legislative, la]
timestamp: "2026-06-20"
---

# Mike Johnson

Current U.S. House of Representatives - LA-4 (Congressional District 4).

## Leadership

- Speaker of the House (since 2025-01-03)
```

The format conforms to the [Open Knowledge Format (OKF)](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md): only `type` is strictly required, unknown keys are tolerated, and the concept ID is the file path. Republic OS layers a stricter, schema-validated profile on top — see [`/schemas`](../schemas).

## Entity types

| `type` | Count | Home | Schema |
|---|---:|---|---|
| **Person** | 13,329 | `us/people/`, `us/states/<st>/…/people/` | [person.schema.json](../schemas/person.schema.json) |
| **Body** | 275 | `us/bodies/…`, `us/executive/…` | [body.schema.json](../schemas/body.schema.json) |
| **Candidate** | 2,494 | `us/states/<st>/candidates/` | [candidate.schema.json](../schemas/candidate.schema.json) |
| **Jurisdiction** | 29,905 | county / city `index.md`, `us/states/<st>/districts/` | [jurisdiction.schema.json](../schemas/jurisdiction.schema.json) |
| **LegalText** | 11,221 | `legal/us/code/title-<nn>/…` | [legal_text.schema.json](../schemas/legal_text.schema.json) |

- **Person** — an officeholder, filed by the jurisdiction they serve. Federal members are enriched with their bioguide ID, leadership roles, and committee seats.
- **Body** — an institution: a chamber, committee, subcommittee, or an executive department/agency/office. The "repos" of the government-as-code model. Executive Bodies under `us/executive/` are minted from the Code's own enumerations (5 U.S.C. §§ 101, 5312) and carry the **authority axis** — reciprocal links to the U.S. Code sections that empower them, from `data/section_authority_edges.jsonl`.
- **Candidate** — someone running for office, distinct from a current officeholder. Sourced from FEC filings.
- **Jurisdiction** — a place with a government, carrying Census demographics and/or district edges. A county's node is its directory `index.md`; a **city's** is likewise an `index.md` under `municipalities/`, keyed by Census place GEOID and modelled exactly like a county (place + government fused, officeholders nested beneath); a district's is a file under `districts/`.
- **LegalText** — a single section of statute, filed under its title and chapter. See the [legal corpus](legal-corpus.md).

## The jurisdiction tree

Geography is a hierarchy: every entity sits in exactly one place in the tree. The schema is **fractal** — a county commissioner and a U.S. senator are both `Person`; a school board and the House are both `Body` — so the same shapes repeat at every level.

```
data/jurisdictions/
  us/
    people/                         federal officeholders (542)
    bodies/                         House, Senate, committees, subcommittees
      house/committees/…
      senate/committees/…
    states/
      fl/
        people/                     FL state legislators
        candidates/                 2026 federal candidates from FL
        districts/                  congressional districts (ACS demographics)
        counties/
          st-lucie/
            index.md                the county as a Jurisdiction node
            people/                 county officeholders
            municipalities/
              port-st-lucie/
                index.md            the city as a Jurisdiction node (GEOID)
                people/             city officeholders
```

The tree is **complete on the map, uneven on the ground**: every U.S. county *and* every incorporated municipality (19,513 of them) exists as a node, but officeholder depth is deepest in Florida and thins out elsewhere. A city node with no `people/` yet is a truthful skeleton stub — "governed, not yet mirrored." An empty directory is not a failure — it is the frontier.

A second axis — cross-cutting **issues** that link entities across the tree — is designed but not yet built. See the [roadmap](roadmap.md).

## Identifiers

- **Path is identity.** The concept ID is the file path (OKF): `us/states/fl/counties/st-lucie/people/anthony-bonna` is both the address and the ID. Paths use lowercase slugs and stable government identifiers where available.
- **Carried IDs** round-trip back to sources: Atlas UUIDs (`person`, `office`, `tenure`, `jurisdiction`), `bioguide` for federal members, `fec` for candidates, `fips` for counties.
- **Reconciliation** across sources is by normalized name where no shared key exists — for example, congress-legislators (bioguide-keyed) is joined onto Atlas officeholders (UUID-keyed) by name.

## Determinism — why the diffs are trustworthy

The build is deterministic by construction: sorted iteration, a fixed key order, one full rebuild per run. `make build` twice produces a byte-identical tree, verified by hashing every file. Entity files change **only when the government changes**, never because of pipeline noise (timestamps, ordering, formatting). This is what makes `make changelog` meaningful — a diff is always a real change, never an artifact.

## Validation

[`scripts/validate.py`](../scripts/validate.py) checks all 105,743 files with no third-party dependencies:

1. **OKF conformance** — every file has frontmatter with a non-empty `type`.
2. **Schema conformance** — required fields, property types, and enums per entity type.
3. **Link integrity** — every internal `/`-rooted markdown link resolves to a real file.

It exits non-zero on failure, so it doubles as a CI gate. Run it with `make validate`.
