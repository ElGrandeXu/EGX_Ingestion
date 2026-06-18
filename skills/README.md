# skills

Documentary registry for workspace skills.

Active Codex-discovered repo skills live in `.agents/skills/`. The files under `skills/` are a human-readable mirror for review and maintenance. If a future edit creates divergence, `.agents/skills/` is the active version and must be reconciled first.

Skills:

- `source-ingestion`: ingest exactly one source and produce a decision-oriented note with verdict, scores, risks and production impact.
- `repo-lab-test`: perform a contained GitHub clone, inspection or bounded practical test when it can change the verdict.
- `transversal-synthesis`: synchronize source index, theme map, decisions, production candidates, risks, experiments and handoff after each source.

Maintenance rule:

- Keep each skill focused on one job.
- Keep `name` and `description` in frontmatter.
- Write descriptions with trigger words because implicit invocation depends on them.
- Update `.agents/skills/` first, then mirror here when useful.
