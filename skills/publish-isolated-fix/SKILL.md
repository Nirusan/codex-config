---
name: publish-isolated-fix
description: Use when the user wants to publish only a small, clearly scoped fix from a dirty repo without sweeping in unrelated local changes. Best for requests like "push this", "create the PR", or "ship only this fix" after a targeted change has already been implemented and verified.
---

# Publish Isolated Fix

Use this skill when the user wants a safe publish flow for one small fix while other local work is still in progress.

## Use when

- the repo has unrelated local changes
- the requested publish scope is one file or a very small set of files
- the user wants branch creation, commit, push, or PR creation for only that fix
- the fix was already implemented and only needs careful git handling

## Don't use when

- the whole worktree belongs to the same change
- the task still needs implementation or debugging
- the user wants a broad end-of-session wrap-up
- the repo needs a larger release workflow rather than one isolated fix

## Workflow

1. Inspect scope first.
   - Check `git status --short`, current branch, and the exact diff for the intended files.
   - If the intended scope is not obvious from the conversation and diff, pause and ask which files belong in the publish.
2. Verify before publishing.
   - Use `$completion-verification` for the actual claim being made.
   - Run `$validate-quick` unless the task needs a more specific repro check or the user explicitly skips it.
3. Isolate the fix.
   - If the repo is on `main` or another shared branch, create a dedicated branch with the `codex/` prefix.
   - If already on a dedicated branch that matches the intended scope, stay on it.
   - Stage only the intended files with explicit paths.
4. Commit deliberately.
   - Write a terse commit message that reflects the real fix.
   - Never stage unrelated changes just because they are nearby.
5. Push safely.
   - Push the current branch with upstream tracking if needed.
   - If network or `.git` writes are blocked by sandboxing, request approval instead of working around it.
6. Open the PR when requested or clearly implied.
   - Prefer a draft PR by default.
   - Summarize what changed, why, and how it was validated.
7. Cleanup only after merge and only when requested.
   - Confirm the PR is merged.
   - Delete the remote branch and local branch.
   - Do not auto-pull or auto-rebase `main` if the worktree still has unrelated local changes.

## Safety rules

- Never use `git add .` or `git add -A` in a mixed worktree unless the user explicitly wants the whole tree published.
- Never assume `main` is safe to push from when unrelated local changes exist.
- Never delete branches before confirming the PR is merged.
- Never auto-sync `main` after merge when local changes could create conflicts.
- Prefer explicit file paths, explicit branch names, and explicit PR scope.

## Suggested companions

- `$completion-verification`
- `$validate-quick`
- `$git-add-commit-push`
- `github:yeet`

## Output

Report only the concrete actions taken:

- files staged
- branch created or reused
- commit hash and message
- push result
- PR URL if created
- cleanup actions if performed
