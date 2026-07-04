# Legal Corpus

Republic OS mirrors law as deterministic terrain before it interprets law as intelligence.

The legal pipeline is deliberately mechanical:

```text
official source -> raw snapshot -> normalized legal tree -> manifest -> checksums -> git diff
```

The first legal corpus is a seed import of the United States Code, Title 52,
Voting and Elections, from the Office of the Law Revision Counsel XML release
point current through Public Law 119-100.

## Layout

```text
data/legal/raw/us/code/
  title-52/
    xml_usc52@119-100.zip
    usc52.xml

data/legal/manifests/
  us-code-title-52-119-100.json

data/legal/checksums/
  us-code-title-52-119-100.sha256

legal/us/code/
  title-52/
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
