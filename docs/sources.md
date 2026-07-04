# Sources

Republic OS is a mirror. Every fact in it comes from a public source, and every record carries field-level provenance and a confidence level. This page lists the sources feeding the mirror today; the machine-readable registry is [`data/sources/sources.yaml`](../data/sources/sources.yaml).

The pipeline is **repo-canonical**: raw source exports land in `data/*.jsonl` untouched, and [`scripts/build.py`](../scripts/build.py) generates the entity tree from them in one deterministic pass. Nothing is hand-edited into the tree.

## Active sources

| Source | Feeds | Raw file | Authority |
|---|---|---|---|
| **Atlas / influence.tools** | Officeholders — federal, all state legislatures, FL county + municipal | `officeholders-v2.jsonl` (11,285) | Aggregator |
| **congress-legislators** ([unitedstates project](https://github.com/unitedstates/congress-legislators)) | Bodies, leadership roles, committee memberships | `bodies.jsonl` (233), `leadership.jsonl` (28), `committee_memberships.jsonl` (3,879) | Community, authoritative |
| **FEC** (Federal Election Commission) | 2026 federal candidate filings | `fec_candidates.jsonl` (2,494) | Official |
| **Census ACS 2023** | County & congressional-district demographics | `acs_county.jsonl` (3,231), `acs_cd.jsonl` (363) | Official |

Atlas itself draws from official upstreams — House Clerk XML, Senate.gov XML, OpenStates, Census TIGER/Line geometry, and the Florida Cities partner API — and records the specific upstream in each record's `sources` block. So a Person file's provenance names not just "Atlas" but the document behind the field (e.g. `tenure: House Clerk XML 2026-06-10`).

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
