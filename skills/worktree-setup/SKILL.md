---
name: worktree-setup
description: Use when starting feature work, risky bug fixes, or parallel tasks that would benefit from isolation from the current workspace. Creates or selects a safe git worktree, follows any repo convention already in place, verifies the location is safe if project-local, and establishes a clean baseline before implementation. Do not use when the user explicitly wants the current checkout or the change is truly tiny and low risk.
---

# Worktree Setup

Use this skill when isolation will reduce risk or confusion before implementation.

## Use when

- starting a new feature or multi-file bug fix
- the current checkout already has unrelated changes
- the user explicitly asks for a branch, worktree, or isolated workspace
- you want to validate a change on top of fresh `main` without disturbing ongoing work
- you are splitting work across multiple long-lived tasks

## Don't use when

- the user explicitly wants the current checkout left in place
- the task is truly tiny, low-risk, and the current workspace is already clean
- you only need to inspect or answer questions without changing code

## Goals

- isolate work without scattering random temporary directories
- follow the repository's existing conventions instead of inventing new ones
- verify that the new workspace starts from a known-good baseline

## Workflow

1. Announce that you are setting up an isolated workspace and why it helps for this task.
2. Inspect the current repo state before creating anything:
   - `git status --short --branch`
   - `git worktree list`
   - look for existing conventions such as `.worktrees/`, `worktrees/`, or a clearly established sibling-folder pattern
3. Pick the worktree location using this order:
   - first, follow an existing repo convention if one is already in use
   - otherwise, prefer a project-local `.worktrees/<branch-name>` directory
   - only use a sibling directory when the repo already uses that style or the user asks for it
4. If you use a project-local `.worktrees/` directory, verify it is ignored with `git check-ignore -q .worktrees`.
5. If `.worktrees/` is not ignored, add the minimal ignore rule needed before creating the worktree.
   - Do not auto-commit that ignore change unless the user asks or the repository workflow clearly expects it.
6. Choose the base branch deliberately:
   - use the user-specified base branch when given
   - use fresh `main` or `origin/main` for new work unless continuing an existing feature branch is clearly the right move
   - use the current feature branch when the task is explicitly a continuation of that branch
7. Create the worktree and switch into it.
8. Run only the setup the repo actually needs:
   - install dependencies only if missing or obviously stale
   - use the repo docs or `AGENTS.md` to pick the fastest meaningful baseline check
9. Run a clean baseline verification before implementation.
10. Report:
   - worktree path
   - branch name
   - base branch
   - whether the baseline is clean
   - where subsequent work should happen

## Safety rules

- Prefer one clear convention per repository; do not create a new directory pattern casually.
- Never create stray temporary directories with random suffixes when a repo-local `.worktrees/` folder would do.
- If the baseline check fails, stop and report that clearly before implementing changes.
- Never delete existing worktrees blindly. If cleanup is needed, verify they are not active and ask before removing anything important.
- If the current repo already has a better convention than the default, follow the repo, not the generic rule.

## Recommended baseline checks

Choose the lightest trustworthy baseline for the repo:

- `pnpm build` when build integrity matters most
- `pnpm lint` when lint is the fastest trusted gate
- a targeted test command when the repo has meaningful tests for the area

If the repo docs define a required baseline, follow that instead of improvising.

## Example trigger phrases

- "Create a clean worktree for this feature."
- "Let's work on this without touching my current checkout."
- "Start from latest main in a separate workspace."

## Non-goals

- This skill does not replace implementation planning.
- This skill does not decide the feature scope for you.
- This skill is about safe setup, not cleanup of every branch on disk.
