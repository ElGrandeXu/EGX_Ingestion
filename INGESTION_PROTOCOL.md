# INGESTION_PROTOCOL

Standard pipeline for one source. Do not process a second source until this pipeline is complete for the current one.

## 0. Load context

Read:

- `AGENTS.md`
- `CURRENT_STATE.md`
- `SOURCE_INDEX.md`
- `THEME_MAP.md`
- `DECISIONS.md`
- `PRODUCTION_CANDIDATES.md`
- `RISK_REGISTER.md`
- relevant theme files, if any

Use the active skills in `.codex/skills/` when the task matches them. `.agents/skills/` is a compatibility mirror.
Use `COMMUNICATION_PROTOCOL.md`: no visible checkpoints; write synthesis into files and keep the final user response compressed.

## 1. Identify the source

Capture:

- URL or local reference;
- proposed name;
- author or organization if available;
- source type as metadata;
- ingestion date;
- source ID such as `SRC-0001`;
- user question or decision to unblock.

If the user provides several URLs, select the first unprocessed source and ignore the rest until the current source is complete.

## 2. Determine source type and probable theme

Allowed source types include:

- GitHub repository;
- official documentation;
- technical article;
- discussion thread;
- Hugging Face model, dataset or space;
- architecture or workflow note;
- other.

Assign a probable primary theme. If no active theme fits, create a candidate theme only when the source provides a real signal.

## 3. Read primary evidence

Read the primary source before secondary commentary.

Capture:

- objective and target user;
- claims and evidence;
- setup or operational requirements;
- dependencies and licenses when visible;
- maturity signals;
- architecture or workflow patterns;
- failure modes, risks and noise.

Separate facts, practical proof, opinion, marketing and speculation.

## 4. Decide clone or test

Ask one question: would cloning, local inspection or a command run change the verdict?

Clone/test is justified only if at least one condition is true:

- README or docs are insufficient to score practical value;
- architecture or scripts must be inspected locally;
- an example must be run to validate feasibility;
- production implication depends on a concrete signal;
- a `TEST` verdict needs a bounded experiment.

If clone/test is not justified, state why in the source note.

If clone/test is justified:

- use `repo-lab-test`;
- clone only into `repos/cloned/`;
- read setup files and scripts before commands;
- log external-repo commands in `logs/command-log.md`;
- record conclusion in `EXPERIMENT_LOG.md`.

## 5. Produce the source note

Create a note in `sources/`, using `templates/source-note-template.md` or `sources/_template_source_note.md`.

The note must include:

- metadata and URL;
- short useful summary;
- clone/test decision;
- verdict;
- five scores;
- keep / reject / adapt / test;
- interesting but not priority;
- dangerous, fragile, complex or noisy points;
- impact on `EGX_Production`;
- risks;
- cross-links and next actions.

## 6. Score and decide verdict

Scores:

- Production potential: 1-5
- Practical value: 1-5
- Originality: 1-5
- Implementation complexity: 1-5
- Risk / noise: 1-5

Verdicts:

- `KEEP`: strong, clear value.
- `ADAPT`: useful idea, must be transformed.
- `TEST`: decision depends on a concrete experiment.
- `WATCH`: interesting, not priority now.
- `REJECT`: weak value, too risky, noisy or irrelevant.

Do not use `KEEP` or production-candidate status when practical value is weak.

## 7. Update theme knowledge

For the relevant theme:

- create a folder from `themes/_template_theme/` if needed;
- update sources, patterns, decisions, experiments, production implications and cross-links;
- update `THEME_MAP.md` with maturity, links and implication.

If no theme should be created, state the reason in the source note and `THEME_MAP.md` only when the decision affects the map.

## 8. Update transversal registries

Update:

- `SOURCE_INDEX.md`
- `DECISIONS.md`
- `PRODUCTION_CANDIDATES.md`
- `RISK_REGISTER.md` if a risk exists or changes
- `EXPERIMENT_LOG.md` if a test is run or proposed
- `logs/command-log.md` if any external-repo command was run

Every registry update should be short but decision-oriented.

## 9. Document production impact

Use one of these labels:

- candidate production element;
- indirect influence;
- no impact;
- test required before decision;
- rejected for production.

Production candidates require practical value, risk notes and a next test.

## 10. Handoff

Update `CURRENT_STATE.md`, `NEXT_MISSION.md` and `HANDOFF.md` when:

- a source was ingested;
- an experiment was run or proposed;
- a theme was created, merged, rejected or promoted;
- the next user action changed;
- a blocker exists.

Do not narrate the handoff to the user. Write it into files.

## 11. Final per-source check

Before moving to another source, verify:

- source note exists;
- verdict and scores are present;
- clone/test decision is present;
- source index row exists;
- theme impact is recorded;
- decisions, candidates, risks and experiments are updated or explicitly not needed;
- next action is clear.

Final user response must use the ingestion format in `COMMUNICATION_PROTOCOL.md`.
