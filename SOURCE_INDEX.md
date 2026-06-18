# SOURCE_INDEX

Registry of all ingested sources.

| ID | Name | URL | Type | Status | Ingestion date | Primary theme | Secondary themes | Verdict | Scores | Note | Clone/test decision | Repo clone | Experiment |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| github-dietrichgebert-ponytail | Ponytail | https://github.com/DietrichGebert/ponytail | GitHub repository | ingested | 2026-06-18 | agent-minimalism | token-saving / caveman-final-only; agent portability; benchmark discipline | ADAPT | PP:4 PV:5 O:3 IC:2 RN:3 | `sources/github-dietrichgebert-ponytail.md` | Clone justified because plugin metadata, hooks, tests, skills and benchmarks affect verdict; practical test run locally without installs | Yes: `repos/cloned/ponytail` ignored by git | EXP-0001 done; EXP-0002 done |

## Score format

`PP:x PV:x O:x IC:x RN:x`

- `PP`: Production potential
- `PV`: Practical value
- `O`: Originality
- `IC`: Implementation complexity
- `RN`: Risk / noise

## Status values

- `ingested`: source note and transversal updates complete.
- `test-proposed`: source needs a bounded experiment before final decision.
- `watch`: source kept only as watch signal.
- `rejected`: source rejected with reason documented.
- `blocked`: ingestion cannot continue without missing evidence or user input.

## Maintenance rules

- One row per source.
- Never add fake simulation sources.
- Source type is metadata; themes remain the primary organization axis.
- `Clone/test decision` must say why clone/test was or was not needed.
