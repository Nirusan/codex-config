---
name: implement
description: Use when the user wants to implement a concrete feature, fix a bug, or execute the next planned chunk of work. Reads the relevant local rules, source, tests, and planning context; chooses the next actionable unit when a plan exists; implements carefully; validates the result; and updates related docs or progress when appropriate. Do not use for vague ideation or for end-of-session git finalization alone.
---

# Implement

Use this skill when it is time to actually change code.

## Use when

- the user wants a feature implemented
- the user wants a bug fixed
- a plan already exists and the next story should be executed
- the work is concrete enough to act on now

## Don't use when

- the idea is still vague and needs product discovery
- the main task is architecture planning
- the user only wants to commit, push, or clean up git state

## Goal

Deliver one meaningful chunk of implementation end to end: understand, build, validate, and leave the project clearer than before.

## Workflow

1. Read the local rules first:
   - `AGENTS.md`
   - relevant repo docs
   - the best available planning docs if they exist
2. Inspect the actual implementation surface:
   - run or read `git status --short` to avoid mixing unrelated work
   - read the relevant source, tests, configuration, and existing patterns
   - capture the original repro path, acceptance criteria, or expected behavior when available
3. Determine the work unit:
   - if a plan or progress tracker exists, or the next slice is ambiguous, use `$next-task`
   - otherwise derive a small implementation slice from the user's request
4. If isolation would materially help, use `$worktree-setup` before making changes:
   - dirty worktree with unrelated changes
   - risky or broad edits
   - parallel branch or agent work
5. Make a short execution plan before editing.
6. Implement the smallest coherent slice that moves the task forward.
7. If the work gets blocked by unclear failures, switch to `$systematic-debugging`.
8. Validate the result with the lightest credible checks for the change.
9. If the change establishes a reusable pattern or updates tracked work, use:
   - `$update-docs`
   - `$update-progress`
10. Before claiming readiness, use `$completion-verification`.

## Rules

- Prefer one coherent slice over many half-finished edits.
- Read before editing; avoid patching from assumptions when code, tests, or logs are available.
- Do not auto-commit or auto-push unless the user explicitly asks for git finalization.
- Work with the existing worktree; never revert unrelated user changes.
- Keep the repo's patterns and conventions stronger than your personal preferences.
- Be explicit about assumptions when planning docs are missing or incomplete.
- If the user asked for a small fix, do not balloon it into a refactor unless necessary.

## Validation guidance

Choose the right level for the task:

- targeted command or repro for the behavior changed
- `$validate-quick` for a fast signal
- `$validate` for fuller project validation
- live browser check when UI, layout, or interaction changes
- `$security-check` when the change touches auth, permissions, secrets, or sensitive data
- `$db-check` after schema, migration, or RLS changes

## Output expectations

After using this skill, you should be able to state:

- what was implemented
- what was validated
- what remains open
- whether docs or progress were updated

## Suggested companion skills

- `$next-task`
- `$worktree-setup`
- `$systematic-debugging`
- `$completion-verification`
