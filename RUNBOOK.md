# RUNBOOK

## Mission Start

1. Read `memory/INDEX.n3`.
2. Read relevant N3 cards.
3. Read `doctrine/CORE.md`, `doctrine/MEMORY_HIERARCHY.md` or `doctrine/INGESTION.md` only when needed.
4. Read N2/N1 only when decision-changing.

## One-Source Ingestion

1. Identify one source and the decision question.
2. Capture N1 proof with `templates/source.n1.md` when retained proof is needed.
3. Create one N2 note in `sources/` from `templates/note.n2.md`.
4. Create one N3 card at `memory/<source-id>.n3` from `templates/card.n3.md`.
5. Assign verdict, risk, confidence, production impact and next action.
6. Update `memory/INDEX.n3`, `CURRENT_STATE.md`, `NEXT_MISSION.md` and `HANDOFF.md` when state changes.

## Repo Evidence

Clone or download only when local inspection can change the verdict.
Use `repos/<source-id>/` for temporary N1 repo evidence.
Record decision-changing commands in the N2 note.
Delete temporary repo evidence after synthesis unless retention is explicitly required.

## Verify

Run:

```powershell
.\scripts\check_workspace.ps1
git diff --check
git status --short
```
