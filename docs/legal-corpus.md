# Legal Corpus

Republic OS mirrors law as deterministic terrain before it interprets law as intelligence.

The legal pipeline is deliberately mechanical:

```text
official source -> raw snapshot -> normalized legal tree -> manifest -> checksums -> git diff
```

The legal corpus is the **complete United States Code** — every section of all
53 titles that carry content (Title 53 is reserved and empty), 59,740 records,
from the Office of the Law Revision Counsel USLM XML at release point 119-100
(current through Public Law 119-100). One source, one edition, end to end.

> Pre-v1 note: the raw `.zip`/`.xml` snapshots live off-repo on the depot, not
> in git — only the manifests and checksums (which anchor them by SHA-256) are
> committed. The "raw-first, in-repo" discipline turns on at v1.0. See the
> [README](../README.md#the-disciplines--the-v10-target).

## Layout

```text
data/legal/raw/us/code/          (off-repo pre-v1; hashes committed below)
  title-NN/
    xml_uscNN@119-100.zip
    uscNN.xml

data/legal/manifests/
  us-code-title-NN-119-100.json

data/legal/checksums/
  us-code-title-NN-119-100.sha256

legal/us/code/
  title-NN/
    chapter-101/
      section-10101.md
```

The raw ZIP is the provenance anchor. The generated Markdown is the readable
legal tree. The manifest records source hashes, output hashes, release metadata,
and the section list.

## Discipline

Legal corpus ingestion does not summarize, classify authority, infer
relationships, or answer legal questions. Later layers can extract citations,
definitions, amendments, and authority links from this base. The base itself is
just a reproducible mirror.

## Rebuild

```bash
make legal-us-code
make validate
```

The success condition is that rebuilding from the same pinned source produces
the same normalized legal files and checksums.
