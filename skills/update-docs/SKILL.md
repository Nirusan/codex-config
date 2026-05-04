---
name: update-docs
description: Update durable project documentation after meaningful implementation work. Use when AGENTS.md, README, docs/, SKILL.md, design-system.md, or long-lived memory-bank context should reflect new patterns, integrations, setup, or behavior. Use update-progress instead for plan/progress trackers.
---

# Update Project Documentation

Update documentation only when the recent work creates durable information future sessions need.

## Scope

Consider existing project docs such as:

- `AGENTS.md`
- `README.md`
- `docs/`
- repo-root `SKILL.md`
- `design-system.md`
- durable `memory-bank/` context files

Do not use this skill for plan/progress trackers; use `$update-progress` instead.

## Workflow

1. Gather evidence from the actual change:
   - `git diff` or staged diff
   - files modified
   - tests or validation output when relevant
   - decisions or constraints that changed during implementation
2. Identify docs that already describe the changed area.
3. Decide whether an update is meaningful:
   - new reusable pattern or convention
   - new setup, dependency, integration, or environment variable
   - changed user-facing behavior or operational flow
   - bug fix that revealed a durable constraint
   - validation or deployment rule future work must know
4. Skip updates when the information is obvious, one-off, duplicative, speculative, or already covered.
5. Apply minimal edits in the existing style.

## Rules

- Never read or modify `memory-bank/brainstorm.md`.
- Prefer updating existing sections over adding new docs.
- Do not create a new documentation structure unless the repo already uses that pattern or the user asks.
- Keep `AGENTS.md` concise and scannable.
- Do not document unverified claims as facts.

## Output

Return a concise report:

- docs inspected
- docs updated
- evidence used
- no-op decisions and why
