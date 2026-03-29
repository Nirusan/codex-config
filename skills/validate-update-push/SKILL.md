---
name: validate-update-push
description: Use when the user explicitly wants an end-of-task or end-of-session wrap-up that includes validation, documentation or progress sync if relevant, and git finalization. Runs the appropriate verification first, updates tracked docs only when needed, and commits or pushes only if that is part of the request.
---

# Validate, Update, and Push

Use this skill as a macro wrapper for careful finalization.

## Use when

- the user says "finalize", "wrap up", or "ship it"
- the user wants a full end-of-task cleanup including validation and git
- the branch should be left in a well-documented, validated state

## Don't use when

- the user only wants a quick pass/fail check
- the work is still in active implementation or debugging
- the user does not want git finalization

## Workflow

1. Run `$completion-verification` first to align proof with the actual claim.
2. Run `$validate` or `$validate-quick` as appropriate for the task and repo.
3. If the work changed reusable patterns or tracked project state, run:
   - `$update-docs`
   - `$update-progress`
4. If the user wants git finalization, use `$git-add-commit-push`.
5. Summarize what was:
   - verified
   - updated
   - committed
   - pushed

## Rules

- Do not treat project validation alone as proof that a specific bug is fixed.
- Do not update docs or progress when nothing meaningful changed.
- Do not commit or push just because validation passed; that still depends on user intent.
- If any validation fails, stop and report the failure before moving to docs or git.

## Output

Return a short structured wrap-up with:

- verification performed
- doc/progress updates made or skipped
- git actions performed or skipped
- anything still unverified
