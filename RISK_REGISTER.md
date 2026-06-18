# RISK_REGISTER

Risk registry.

| ID | Date | Type | Description | Source / theme | Severity 1-5 | Trigger | Mitigation | Status |
|---|---|---|---|---|---:|---|---|---|
| RISK-0001 | 2026-06-18 | Ingestion/production confusion | Risk of turning research notes into production architecture too early | Workspace | 3 | Production candidate proposed without score, proof or next test | Keep `EGX_Ingestion` separate from `EGX_Production`; require scoring, tests and decisions | Active |
| RISK-0002 | 2026-06-18 | Skill divergence | `.agents/skills/` and `skills/` can diverge if future edits update only one copy | Workspace | 2 | Skill behavior changes in one location only | Treat `.agents/skills/` as active and `skills/` as documentary mirror | Active |

## Types to watch

- Heavy dependencies
- Unstable repositories
- Hype without substance
- Excessive complexity
- Security
- Workspace pollution
- Ingestion/production confusion
- Risky commands
- Low-quality sources
- License or usage constraints

## Status values

- `Active`
- `Mitigated`
- `Accepted`
- `Closed`

## Maintenance rules

- Add risks when they affect a source verdict, experiment, production candidate or workspace health.
- Do not add vague fear. State trigger and mitigation.
