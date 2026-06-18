# THEME_MAP

Living map of themes. Themes emerge from sources; they are not predefined by platform.

## Active themes

| Theme | Maturity 1-5 | Sources | Current decision question | EGX_Production implication | Notes |
|---|---:|---|---|---|---|
| agent-minimalism | 3 | github-dietrichgebert-ponytail; EXP-0002 | Can agents reduce code/dependency/abstraction bloat without cutting safety or checks? | Candidate adapted ladder validated for EGX_Ingestion; production still needs a production-style task | Distinct from communication/token saving; plugin installation rejected |

## Candidate themes

| Candidate theme | Trigger source | Why track it | Next decision |
|---|---|---|---|
| _No candidate yet_ | - | - | - |

## Merged themes

| Former theme | New theme | Date | Reason |
|---|---|---|---|
| _None yet_ | - | - | - |

## Rejected themes

| Theme | Date | Reason | Sources |
|---|---|---|---|
| _None yet_ | - | - | - |

## Links between themes

| Theme A | Relation | Theme B | Evidence | Impact |
|---|---|---|---|---|
| agent-minimalism | complements but is distinct from | token-saving / caveman-final-only | Ponytail governs implementation choices; Caveman governs user-visible communication | Keep code economy and speech economy separate in future doctrine |
| agent-minimalism | supports | agent portability | Ponytail centralizes core skills and verifies host-specific copies | Future portable rules need drift checks before promotion |
| agent-minimalism | supports | benchmark discipline | Ponytail documents corrected agentic benchmark claims after critique | Use reproducible agentic tests before adopting source claims |

## Maturity scale

1. Isolated signal
2. Candidate theme
3. Active theme
4. Validated by tests or convergent sources
5. Ready for production decision

## Maintenance rules

- Theme names should describe a practical pattern or decision area, not a platform.
- Update this file after each source when a theme is created, rejected, merged, promoted or linked.
- Keep rejected themes visible to avoid repeating weak patterns.
