---
name: completion-verification
description: Use before claiming work is ready, fixed, safe to merge, or ready to commit or push. Requires fresh task-appropriate verification and reporting only what was actually observed. Use this especially when you are about to say that a bug is fixed, that a build passes, or that a feature is ready. Do not use as a substitute for debugging or implementation.
---

# Completion Verification

Use this skill to make completion claims based on fresh evidence, not confidence.

## Use when

- about to say "done", "ready", "fixed", "safe to merge", or "safe to push"
- before commit, push, PR, or deployment-related conclusion
- after a bug fix when the original symptom must be rechecked
- after a UI change when behavior or layout should be confirmed visually
- after a security-sensitive change when auth or ownership behavior must still be true

## Don't use when

- still in the middle of diagnosis
- still actively implementing major code changes
- the user only wants brainstorming or planning

## Core rule

Match the proof to the claim, then run that proof freshly.

## Verification workflow

1. Identify the exact claim you are about to make.
   - "The build passes"
   - "The bug is fixed"
   - "This is ready to merge"
   - "The revoke flow works now"
2. Identify the freshest proof that matches that claim.
3. Run it now, not based on a previous run unless nothing changed and you state that explicitly.
4. Read the actual output or behavior.
5. Report only what the evidence proves.
6. If something could not be verified, say that plainly and lower the confidence accordingly.

## Match proof to claim

### Build / type / integration claim

Use the repo's real validation command, commonly:

- `pnpm build`
- `pnpm lint`
- relevant tests if they exist and matter

### Bug fix claim

Re-run the original repro path or the closest faithful equivalent.

### UI claim

Check the UI in a live browser, at the relevant viewport(s), and confirm the specific interaction or layout.

### Security / auth claim

Verify the allowed and denied paths, not just the happy path.

### Migration or database claim

Confirm the migration applies and the intended data path behaves correctly.

### Commit / push / PR claim

Verify the git state and review scope before saying work is safe to commit, push, or open as a PR:

- `git status --short --branch`
- staged diff or intended diff scope
- current branch and remote target
- relevant CI/check status when available

## Recommended companions

- Use `$validate-quick` for a compact pass/fail health check.
- Use `$validate` when you need fuller validation output.
- Use `$security-check` when the claim involves auth, permissions, secrets, or sensitive data.

## Output style

Prefer concise evidence statements such as:

- `pnpm build`: passed
- original repro: no longer reproduces
- UI check on desktop and mobile: matches expected behavior
- git scope: staged diff contains only intended files
- not verified: production-only webhook path

## If verification fails

- do not reframe the claim to sound successful
- report what failed
- say what remains blocked
- return to implementation or debugging as needed

## Anti-patterns

- "should work now"
- "looks good to me" without a run
- "build should pass" after only linting
- saying a bug is fixed because the code path changed
- relying on stale output from before the last edits

## Example trigger phrases

- "Is it ready?"
- "Can we commit?"
- "Can we push this?"
- "Does it build?"
- "Are we good to merge?"

## Non-goals

- This skill does not decide product scope.
- This skill does not debug the issue for you.
- This skill is about honest completion signals, not exhaustive QA in every case.
