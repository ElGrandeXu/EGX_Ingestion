# SOURCE_INDEX

Registry of all ingested sources.

| ID | Name | URL | Type | Status | Ingestion date | Primary theme | Secondary themes | Verdict | Scores | Note | Clone/test decision | Repo clone | Experiment |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| _No source ingested yet_ | - | - | - | - | - | - | - | - | - | - | - | No | No |

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
