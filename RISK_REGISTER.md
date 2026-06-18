# RISK_REGISTER

Risk registry.

| ID | Date | Type | Description | Source / theme | Severity 1-5 | Trigger | Mitigation | Status |
|---|---|---|---|---|---:|---|---|---|
| RISK-0001 | 2026-06-18 | Ingestion/production confusion | Risk of turning research notes into production architecture too early | Workspace | 3 | Production candidate proposed without score, proof or next test | Keep `EGX_Ingestion` separate from `EGX_Production`; require scoring, tests and decisions | Active |
| RISK-0002 | 2026-06-18 | Skill divergence | `.codex/skills/`, `.agents/skills/` and `skills/` can diverge if future edits update only one copy | Workspace | 3 | Skill behavior changes in one location only | Treat `.codex/skills/` as primary, `.agents/skills/` as compatibility mirror and `skills/` as documentary mirror; verify with `check_workspace.ps1` | Active |
| RISK-0003 | 2026-06-18 | Communication compression | Final-only output could hide a real blocker or make a technical decision ambiguous | Workspace | 2 | Mission cannot proceed safely, exact error matters, or final compression drops critical context | Use blocker exception format and preserve exact paths, commands, errors and verdicts | Active |
| RISK-0004 | 2026-06-18 | Plugin sprawl | Installing agent plugins too early can add hooks, hidden state and instruction conflicts before local value is proven | github-dietrichgebert-ponytail / agent-minimalism | 4 | A source recommends marketplace/plugin install before EGX has tested the method | Ingest as evidence only; do not install Ponytail; prefer checklist or review experiment first | Active |
| RISK-0005 | 2026-06-18 | Minimalism / negligence confusion | Code minimization can accidentally remove validation, error handling, security or accessibility | agent-minimalism | 4 | Minimal implementation rule is applied without safety carve-outs | Require explicit safety carve-outs and one runnable check for non-trivial logic | Active |
| RISK-0006 | 2026-06-18 | Always-on rule cost | Reinjecting implementation-minimalism rules every turn can increase context cost or compete with mission instructions | github-dietrichgebert-ponytail / agent-minimalism | 3 | A ruleset is made always-on instead of used selectively | Test review/checklist mode before any always-on skill; keep Caveman final-only separate | Active |
| RISK-0007 | 2026-06-18 | Benchmark hype | LOC and cost claims can be misleading when baseline, safety checks or agent isolation are weak | github-dietrichgebert-ponytail | 3 | Source promotes headline reduction numbers without caveats | Preserve benchmark limitations; rely on agentic tests and source inspection over marketing numbers | Active |

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
