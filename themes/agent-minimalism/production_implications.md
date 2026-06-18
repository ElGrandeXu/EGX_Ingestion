# Production Implications

## Candidate elements

- Adapted minimal implementation ladder:
  - YAGNI first.
  - Standard library first.
  - Native platform first.
  - Existing dependency before new dependency.
  - Minimum working implementation.
  - Safety carve-outs are not optional.
  - Non-trivial logic gets one runnable check.

- EGX-specific extension:
  - Reuse existing doctrine, registers and templates before new files.
  - Prefer Markdown decisions over scripts when automation is not needed.
  - Prefer local contained experiments over global installs.
  - Promote to production only after evidence and decision records.

## Required proof

- A second production-style implementation experiment showing reduced unnecessary code or dependencies.
- Evidence that validation, security, accessibility and data-loss protection are not cut.
- A decision on whether this belongs as checklist, review skill, or always-on instruction in `EGX_Production`.

## Risks

- Minimalism can become underbuilding if safety floors are omitted.
- Always-on rules can consume context and conflict with task-specific instructions.
- Plugin installation can add hidden state or hooks outside the intended workspace behavior.

## Open questions

- Should future production use this as a review checklist only, or as durable repo instruction?
- Should shortcut debt be tracked in a general debt file or only inline with comments?
- Does this improve real EGX_Production tasks enough to justify a repo-scoped skill?
