# INGESTION

## Protocol

Process exactly one source at a time.

Every future ingestion produces:

- N1 proof or proof pointer;
- one N2 note in `sources/`;
- one N3 card at `memory/<source-id>.n3` from `templates/card.n3.md`;
- verdict: `KEEP`, `ADAPT`, `REJECT` or `WATCH`;
- risk, confidence, production impact and next action.

## Traceability

N3 points to N2 and N1 when they exist. N2 records the decision question, evidence, command output that affected the verdict, risks, rejected material and next action.

## Repo Evidence

Use local repo inspection only when it can change the verdict. Put temporary repo evidence under `repos/<source-id>/`, read setup files before commands, record decision-changing commands in N2, then delete the repo unless explicit retention is required.

## Completion Rule

An ingestion is incomplete if it ends with only a summary. It must produce source -> synthesis -> decision.
