# COMMUNICATION_PROTOCOL

Canonical communication rule for `EGX_Ingestion`.

## 1. Default: final-only

- Codex works silently during execution.
- No step narration.
- No progress checkpoints.
- No live reasoning explanation.
- No "I will" announcements.
- Work first, deliver final result only.

## 2. Allowed interruptions

Interrupt only for:

- user authentication required;
- secret or token required;
- destructive action outside scope;
- total technical blocker;
- irreversible choice;
- system permission required;
- risk of modifying outside `C:\Users\maxer\Desktop\EGX_Ingestion`.

## 3. Default final format

```text
status: done | partial | blocked
changed:
* essential files
verified:
* checks executed
decision:
* main decision
next:
* next action
```

## 4. Ingestion final format

```text
status:
source:
verdict:
scores:
theme:
kept:
rejected:
tested:
updated:
next:
```

## 5. Error format

```text
status: blocked
blocker:
evidence:
needed:
safe next:
```

## 6. Style bans

Do not write:

- "J'ai commence par..."
- "Ensuite, j'ai..."
- "Voici ce que j'ai fait en detail..."
- "Bonne nouvelle..."
- "Parfait..."
- "Je vais maintenant..."
- long justification paragraphs;
- decorative tables;
- long raw logs;
- repeated full paths unless useful;
- summary plus duplicate details.

## 7. Exactness preserved

- Preserve exact paths when needed.
- Preserve exact commands.
- Quote exact errors when decisive.
- Keep verdicts blunt.
- Do not compress technical decisions into ambiguity.
- Write in French when the user writes in French.
