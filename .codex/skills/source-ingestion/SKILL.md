---
name: source-ingestion
description: Use when ingesting exactly one technical source and producing a decision-oriented source note with URL, source type, themes, clone/test decision, verdict, scores, risks, cross-links, and EGX_Production impact.
---

# Source Ingestion

Use this skill for exactly one source at a time. Do not process another source until transversal synthesis is complete.

## Inputs

- Source URL or local reference.
- Optional user note explaining why it matters.
- Current `SOURCE_INDEX.md`, `THEME_MAP.md`, `DECISIONS.md`, `PRODUCTION_CANDIDATES.md`, `RISK_REGISTER.md`.
- Relevant theme files if a theme already exists.

## Steps

1. Assign or confirm a source ID such as `SRC-0001`.
2. Capture URL, name, author or organization, source type, ingestion date and user decision question.
3. Read the primary source before secondary commentary.
4. Extract practical claims, evidence, architecture patterns, workflows, dependencies, license signals, maturity signals and risks.
5. Decide whether clone or practical test is necessary. State why.
6. Choose or propose one primary theme and optional secondary themes.
7. Create a source note in `sources/` using `templates/source-note-template.md` or `sources/_template_source_note.md`.
8. Assign verdict: `KEEP`, `ADAPT`, `TEST`, `WATCH` or `REJECT`.
9. Assign scores 1-5: Production potential, Practical value, Originality, Implementation complexity, Risk / noise.
10. State what to keep, reject, adapt, test, what is interesting but not priority, and what is dangerous, fragile, complex or noisy.
11. State the impact on `EGX_Production`: candidate, indirect influence, no impact, test required or rejected.
12. Hand off to `transversal-synthesis` before moving to another source.

## Output

- One source note in `sources/`.
- A clear verdict and five scores.
- Clone/test decision.
- Risks and production implication.
- Required transversal updates.

## Failure condition

If the output is only a summary, the ingestion is incomplete.
