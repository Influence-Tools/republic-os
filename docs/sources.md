# Sources

Republic OS is a mirror. Every fact in it comes from a public source, and every record carries field-level provenance and a confidence level. This page lists the sources feeding the mirror today; the machine-readable registry is [`data/sources/sources.yaml`](../data/sources/sources.yaml).

The pipeline is **repo-canonical**: raw source exports land in `data/*.jsonl` untouched, and [`scripts/build.py`](../scripts/build.py) generates the entity tree from them in one deterministic pass. Nothing is hand-edited into the tree.

## Active sources

| Source | Feeds | Raw file(s) | Authority |
|---|---|---|---|
| **Atlas / influence.tools** | Officeholders — federal, all state legislatures, FL county + municipal | `officeholders-v3.jsonl` (13,329) | Aggregator |
| **Atlas / PostGIS** | Exact Census place GEOID per municipal officeholder | `officeholders-municipal-geoid.jsonl` (3,979) | Derived (Census places) |
| **congress-legislators** ([unitedstates project](https://github.com/unitedstates/congress-legislators)) | Bodies, leadership roles, committee memberships | `bodies.jsonl` (233), `leadership.jsonl` (28), `committee_memberships.jsonl` (3,879) | Community, authoritative |
| **FEC** (Federal Election Commission) | 2026 federal candidate filings | `fec_candidates.jsonl` (2,494) | Official |
| **Census ACS 2023** | County & congressional-district demographics | `acs_county.jsonl` (3,231), `acs_cd.jsonl` (363) | Official |
| **Census places + PostGIS** (via Atlas) | Place → county crosswalk behind the 19,513 municipal nodes | `place_county_crosswalk.jsonl` (32,041) | Official (Census) |
| **Census TIGER 2024 + PostGIS** (via Atlas) | County → congressional/state-leg district area-overlap edges | `county_district_edges.jsonl` (16,328) | Official (Census) |
| **U.S. Code** — OLRC USLM XML, release point 119-100 | The complete legal corpus: every section of all 53 populated titles | `legal/us/code/**` (59,740) | Official (Office of the Law Revision Counsel) |
| **U.S. Code, Title 5** (§§ 101, 5312) | The executive-branch node layer — 15 departments + 21 Level I offices | `executive_offices.jsonl` (21) | Derived from official statute |
| **U.S. Code** (all titles) | The authority axis — § → executive office it empowers | `section_authority_edges.jsonl` (27,804) | Extracted from official statute |

Atlas itself draws from official upstreams — House Clerk XML, Senate.gov XML, OpenStates, Census TIGER/Line geometry, and the Florida Cities partner API — and records the specific upstream in each record's `sources` block. So a Person file's provenance names not just "Atlas" but the document behind the field (e.g. `tenure: House Clerk XML 2026-06-10`).

The **legal corpus** is mirrored directly from the official OLRC USLM XML (no aggregator), pinned at release point 119-100 with per-title manifests and SHA-256 checksums. Pre-v1, the raw `.zip`/`.xml` snapshots live off-repo on the depot (only manifests + checksums are committed); the "raw-first, in-repo" discipline turns on at v1.0 — see the [README](../README.md#the-disciplines--the-v10-target). The **executive nodes and authority edges** are derived deterministically from the Code itself (Title 5's own enumerations, and named-reference extraction across every section) — the mirror mints part of its own structure from the law it holds.

## Provenance in every record

Each entity's frontmatter carries a `sources` list and a `confidence` level:

```yaml
sources:
  - field: tenure
    source: "House Clerk XML 2026-06-10"
  - field: roles
    source: "congress-legislators (unitedstates project)"
confidence: official
```

`confidence` is one of `official`, `reported`, `inferred`, or `unverified`. Everything in the mirror today is `official`.

## Reconciliation and its findings

Sources use different keys — Atlas uses internal UUIDs, congress-legislators uses bioguide IDs, FEC uses committee IDs, ACS uses FIPS codes. Where no shared key exists, records are reconciled by normalized name. Federal officeholders reconcile at ~99% (531 of 532 members matched to their leadership and committee data).

Disagreements between sources are not errors to hide but **findings to surface**. Where Atlas's officeholder roster names a different person for a seat than the authoritative current roster does, the mismatch stands as a visible discrepancy — the gap between the model and reality is itself information.

## Known sources not yet ingested

Named in the [technical brief](../Technical%20Brief%20—%20Government%20as%20Software.md) and [roadmap](roadmap.md), not yet in the mirror: campaign finance flows and contracts (the "money" layer), local agenda portals (Legistar / Granicus / CivicPlus), the Federal Register, lobbying registrations, and property records. These are where the mirror grows next.
