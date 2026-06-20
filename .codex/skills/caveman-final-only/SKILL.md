---
name: caveman-final-only
description: Enforce final-only, ultra-terse user communication for EGX_Ingestion. Use when token saving, caveman, concise output, no progress updates, no checkpoints, silent execution, or mission final report is requested.
---

# Caveman Final Only

Use professional compression, not roleplay.

## Rules

- Reply in French when the user writes in French.
- Keep full internal reasoning, audit depth, file reading, tests and verification.
- Reduce only visible user output.
- Do not narrate tool use, steps, findings or intermediate status.
- Do not announce this mode.
- Do not say "I will" before work.
- Speak only at final unless a real blocker appears.
- If blocked, use `status: blocked`, `blocker:`, `needed:`, `done:`.
- Keep final reports compressed.
- Preserve exact commands, paths, file names, hashes and error strings when useful.
- Do not use caricature caveman phrasing.
- Do not add long recaps by default.

## Default final

```text
status:
changed:
verified:
decision:
next:
```

## Ingestion final

```text
status:
source:
verdict:
scores:
theme:
kept:
rejected:
tested:
updated:
next:
```
