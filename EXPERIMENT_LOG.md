# EXPERIMENT_LOG

Journal of practical tests and proposed experiments.

| ID | Date | Repo / source | Theme | Status | Command or inspection | Objective | Result | Errors | Conclusion | Decision impact |
|---|---|---|---|---|---|---|---|---|---|---|
| EXP-0001 | 2026-06-18 | github-dietrichgebert-ponytail | agent-minimalism | done | `npm test`; `node scripts\check-rule-copies.js`; `npm test --prefix pi-extension`; environment checks `python --version`, `python -c "import pandas"`, `node --version`, `npm --version` | Verify local repo maturity without installing Ponytail or dependencies | `node scripts\check-rule-copies.js` passed; `npm test --prefix pi-extension` passed 11 tests; root `npm test` passed 50 tests and failed 1 pandas-dependent CSV correctness test | `ModuleNotFoundError: No module named 'pandas'` caused `csv: correct pandas one-liner passes` failure | Repo structure and core adapter tests are credible; full suite needs pandas, but no install was forced | Supports ADAPT verdict; does not justify plugin install |
| EXP-0002 | 2026-06-18 | github-dietrichgebert-ponytail | agent-minimalism | proposed | Future bounded implementation comparison | Test adapted minimal implementation ladder against a normal implementation task | Not run | None | Required before promoting candidate into `EGX_Production` doctrine | Keeps PC-0001 as `test-required` |

## Status values

- `proposed`
- `running`
- `done`
- `blocked`
- `cancelled`

## Rules

- Every external-repo command must also be documented in `logs/command-log.md`.
- Errors useful for a decision must be preserved in summary form.
- An experiment must produce a decision-oriented conclusion.
- Experiments stay contained in `EGX_Ingestion`.
- A `TEST` verdict must create a proposed or completed experiment entry.
