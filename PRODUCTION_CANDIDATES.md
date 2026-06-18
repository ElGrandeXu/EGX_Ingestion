# PRODUCTION_CANDIDATES

Elements that could later migrate to `EGX_Production`.

| ID | Pattern / element | Source | Theme | Status | Practical value evidence | Confidence 1-5 | Estimated effort | Risk | Next test |
|---|---|---|---|---|---|---:|---|---|---|
| PC-0001 | Adapted minimal implementation ladder | github-dietrichgebert-ponytail | agent-minimalism | test-required | Ponytail repo provides cross-agent rules, safety carve-outs, examples, benchmarks and passing local rule-copy/pi-extension tests | 4 | Low if used as checklist; medium if made a repo-scoped skill | Minimalism can become underbuilding; always-on context can conflict with task-specific requirements | EXP-0002: bounded implementation comparison before migration |

## Entry rules

- Do not add an idea only because it is original.
- Require clear practical value.
- Require a source note, risk note and next test or reason no test is needed.
- Prefer `ADAPT` and `TEST` over premature production promotion.

## Exit or downgrade rules

- Remove or downgrade candidates that become too complex, fragile, risky or noisy.
- Downgrade when practical value is not confirmed after testing.
- Reject candidates with unclear license, unsafe behavior or disproportionate dependency burden.

## Status values

- `candidate`
- `test-required`
- `accepted-for-future-migration`
- `rejected`
- `archived`
