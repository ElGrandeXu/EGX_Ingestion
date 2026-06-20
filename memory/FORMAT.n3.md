# FORMAT.n3

Canonical N3 card format:

```text
ID=<stable-id>
TYPE=<source|theme|decision|risk|candidate|mission>
V=<KEEP|ADAPT|REJECT|WATCH|ACTIVE|BLOCKED>
TH=<theme-or-none>
RISK=<LOW|MED|HIGH>
PROD=<YES|NO|MAYBE>
CONF=<LOW|MED|HIGH>
N2=<path-or-none>
N1=<path-or-none>
NEXT=<short-action>
WHY=<short-reason>
```

Rules:

- One field per line.
- Short values only.
- Workspace-relative paths.
- A card must allow a fast decision.
- A card is not literary summary.
- A card points to N2 and N1 when they exist.
- Long detail belongs in N2 or N1.

Default export: `memory/exports/<source-id>-N3.md`.

Frontmatter fields:

```yaml
title:
source:
ingestion_date:
verdict:
confidence:
tags:
next_action:
model_used:
tokens:
density_score:
```

After frontmatter, write the same compact N3 card fields.
