# The Legislation Corpus

Enacted state legislation, all 50 states — the *merged pull requests* of
American law, where the U.S. Code corpus is the deployed branch.

## What's here

197,131 records under `legislation/us/states/{st}/{session}/`, one file per
enacted bill or resolution, from the OpenStates bulk snapshot vintage
**2026-07-01**. Each record carries the bill's version chain (the diff),
action timeline (the PR events), sponsors (the authors), roll-call votes (the
merge decisions), and a `source_hash` over the raw record.

**"Enacted" includes joint and concurrent resolutions**, not only bills — the
`classification` frontmatter field records which. Some states resolve
prolifically (Tennessee's 22,173 enacted = 8,785 bills + 13,388 joint
resolutions); the mirror records what the legislature enacted and leaves
filtering to views.

A bill is a pull request against the law: filed, revised through committee
substitutes (the commits), voted on (the reviews), and — if it passes and is
signed — merged. Enacted bills are the ones that merged.

## Provenance

- Source: OpenStates bulk snapshot (`data.openstates.org`), aggregated from
  official legislature sites. Confidence: `reported`.
- Raw JSONL (~1.1 GB, 50 files) lives off-repo on the depot at
  `/exports/legislation/2026-07-01/`; the committed anchor is
  [`data/sources/legislation_manifest_2026-07-01.json`](../data/sources/legislation_manifest_2026-07-01.json)
  with per-state SHA-256, byte counts, and record counts.
- Rebuild: `make legislation` (requires the depot mount; `LEG_STATES="fl ca"`
  and `LEG_VINTAGE=` overridable). Deterministic — rerun is byte-identical.

## Next vintages

A future OpenStates snapshot re-exported over this tree surfaces *only real
legislative change* as diffs — new bills, new actions, new enactments. The
difference between two vintages is the changelog of American state law.

## Not yet

No bill → sponsor edges to `Person` nodes yet — that needs name reconciliation
(the OpenStates `person_id` is not the repo's identity), a follow-on axis like
the committee-seat and authority edges. And no bill *text*: the version chain
records the diff points and links to each version's source document, but the
statutory text itself is not mirrored in this pass.
