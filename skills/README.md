# skills

Documentary registry for workspace skills.

Primary Codex repo-scoped skills live in `.codex/skills/`. `.agents/skills/` is a compatibility mirror. The files under `skills/` are a human-readable mirror for review and maintenance. If a future edit creates divergence, `.codex/skills/` is the active version and must be reconciled first.

Skills:

- `caveman-final-only`: final-only, ultra-terse user communication without reducing analysis, tests or verification.
- `source-ingestion`: ingest exactly one source and produce a decision-oriented note with verdict, scores, risks and production impact.
- `repo-lab-test`: perform a contained GitHub clone, inspection or bounded practical test when it can change the verdict.
- `transversal-synthesis`: synchronize source index, theme map, decisions, production candidates, risks, experiments and handoff after each source.

Maintenance rule:

- Keep each skill focused on one job.
- Keep `name` and `description` in frontmatter.
- Write descriptions with trigger words because implicit invocation depends on them.
- Update `.codex/skills/` first, mirror to `.agents/skills/` for compatibility when useful, then mirror here when useful.
