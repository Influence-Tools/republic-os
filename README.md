# Republic OS

An open, version-controlled mirror of public power in the United States.

Government is already software: statutes are code, agencies are processes, elections change the maintainers, and a bill is a pull request against the law. What government has never had is a changelog. This repository is that changelog.

**The diff is the product.** Every file here mirrors the observable public state of a government entity — people, offices, bodies, meetings, organizations, money, issues — as deterministic, sourced, human-readable records. When government changes, the files change, and git makes the change visible, permanent, and inspectable.

- **Founding document:** [Technical Brief — Government as Software](Technical%20Brief%20—%20Government%20as%20Software.md)
- **Format:** Markdown + YAML frontmatter ([OKF](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md)-conformant), validated by JSON Schema
- **Data:** raw source exports land in `data/` first; refinement into structured entity files is itself a visible diff
- **Substrate for:** [influence.tools](https://influence.tools)

Three disciplines govern everything here: never overwrite, never rewrite history, always push off-box.
