# NEXT_MISSION

Mission: ingest one new technical or methodological source.

Constraints:

- Start from `memory/INDEX.n3`.
- Process one source only.
- Clone only if local inspection can change the verdict.
- Put temporary repo evidence under `repos/<source-id>/`.
- Delete clones after synthesis unless explicitly retained.
- Do not modify production workspaces.
- Apply agent-minimalism before adding structure.

Done when:

- N1 proof identified.
- N2 source note created in `sources/`.
- N3 source card created at `memory/<source-id>.n3` from `templates/card.n3.md`.
- N3 export created at `memory/exports/<source-id>-N3.md`.
- Verdict, scores, risks and production impact are clear.
- `memory/INDEX.n3`, affected N3 cards, `CURRENT_STATE.md` and `HANDOFF.md` are synchronized.
- `.\scripts\check_workspace.ps1` passes.
