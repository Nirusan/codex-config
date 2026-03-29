---
name: git-add-commit-push
description: Use when the user explicitly wants to commit changes, push a branch, or finalize git state after implementation work. Stages only the intended files, checks the repo state before committing, writes a clean commit message, and pushes only when requested or clearly implied. Do not use as a substitute for validation or completion verification.
---

# Git Add, Commit, and Push

Use this skill for deliberate git finalization, not as a default cleanup reflex.

## Use when

- the user explicitly asks to commit
- the user explicitly asks to push
- the user asks to save changes or finalize the branch in git

## Don't use when

- the work is not yet ready
- validation or verification still needs to happen
- the repo contains unrelated changes you have not scoped

## Workflow

1. Inspect the current repo state first:
   - current branch
   - staged vs unstaged changes
   - untracked files
   - remotes and upstream status when push is requested
2. Determine the intended scope of the commit.
   - If the scope is obvious from the conversation and diff, stage only those files.
   - If the repo contains unrelated changes, do not sweep them in silently.
3. Before committing, run `$validate-quick` unless the user explicitly says not to and the risk is clearly acceptable.
4. Craft the commit message:
   - use the user's message if they gave one
   - otherwise generate a concise Conventional Commit style message when appropriate
5. Commit only after the staged scope is intentional.
6. Push only when:
   - the user explicitly asked for push
   - or the user's wording clearly implies remote finalization
7. Report:
   - what was staged
   - the commit hash and message
   - whether anything was intentionally left out
   - whether the branch was pushed

## Staging rules

- Prefer `git add -- <paths>` when the scope is clear.
- Use broader staging only when all current changes are intentionally part of the same unit of work.
- Never default to `git add .` in a dirty repo without checking scope.

## Push rules

- Detect the current branch and upstream instead of forcing `git push -u origin <branch>` every time.
- If upstream is missing and push is requested, set it deliberately.
- If push is not requested, stop at the local commit.

## Commit message rules

- Keep the first line concise.
- Reflect the actual change, not the user's vague request.
- Do not inject a hard-coded co-author footer by default.

## Suggested companions

- `$completion-verification`
- `$validate-quick`
- `$validate`

## Non-goals

- This skill does not decide whether the work is truly ready.
- This skill does not rewrite history unless the user explicitly asks.
