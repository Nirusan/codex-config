---
name: systematic-debugging
description: Use when a bug resists the obvious fix, a test fails unexpectedly, behavior differs across environments, or an integration acts flaky. Focuses on reproducing the issue, gathering evidence, tracing where the failure really starts, comparing working and broken paths, and proving a root-cause hypothesis before editing code. Do not use for purely mechanical text edits or obvious one-line changes with no investigation needed.
---

# Systematic Debugging

Use this skill to debug with evidence instead of guesswork.

## Use when

- a bug is not fully explained yet
- a test or build fails unexpectedly
- browser behavior differs from what the code suggests
- an API, auth flow, SSH flow, or deployment integration is flaky
- one fix attempt did not work and you need a more disciplined approach

## Don't use when

- the task is a pure text or copy change
- the change is obviously mechanical and the failure mode is already fully understood
- the user only wants a high-level explanation, not an actual debug workflow

## Core rule

Do not patch symptoms first. Understand the failure path first.

## Workflow

1. Define the exact symptom.
   - What fails?
   - Where does it fail?
   - What did you expect instead?
2. Reproduce it reliably.
   - Capture the exact command, request, screen, or user flow.
   - If you cannot reproduce it, gather more evidence before proposing fixes.
3. Read the evidence completely before editing code.
   - full error text
   - stack traces
   - console output
   - network responses
   - recent logs
   - recent diffs or commits
4. Trace where the bad state begins.
   - For multi-step systems, inspect each boundary between components.
   - Log or observe what goes in, what comes out, and where expectations first diverge.
5. Find a working comparison whenever possible.
   - similar code path
   - similar endpoint
   - same feature in another environment
   - last known good commit or branch
6. State one hypothesis at a time.
   - Use the form: `I think X is failing because Y evidence points to Z boundary.`
7. Test the smallest change that can validate the hypothesis.
   - one variable at a time
   - no bundled cleanup refactors
   - no "while I'm here" edits
8. Verify the result against the original symptom.
   - Did the exact repro stop failing?
   - Did you create a new issue elsewhere?
9. If one attempt fails, update the hypothesis with the new evidence.
10. If two serious fix attempts fail, widen the investigation instead of stacking more guesses.

## Evidence to gather by context

### Browser and UI issues

- use the browser directly before editing
- inspect console, network, screenshots, and visible state
- compare what the user sees to what the code assumes
- use Browser Use / the Codex in-app browser when a live browser check is useful, with `$dev-browser` as a fallback if Browser Use is unavailable or insufficient

### Auth, permissions, and security-sensitive flows

- verify the real user, token, ownership check, and response path
- compare allowed vs denied cases
- use `$security-check` when the issue touches authorization or sensitive data

### Database and migration issues

- inspect the exact query path, mutation path, and schema assumptions
- verify policies and permissions instead of assuming them
- use `$db-check` after DB changes or when RLS/security smells involved

### Infra and integration issues

- confirm connectivity first
- separate transport errors from application errors
- inspect logs on both sides of the integration if possible

## Output expectations

Before the fix, be able to state:

- symptom
- evidence
- likely boundary where the failure starts
- current hypothesis
- smallest validating action

After the fix, be able to state:

- what changed
- what evidence now passes
- what remains uncertain, if anything

## Anti-patterns

- "This probably fixes it."
- applying several edits before retesting
- rewriting code before reading the error fully
- treating absence of an error message as proof of success
- declaring victory because the code looks reasonable

## Example trigger phrases

- "This still fails and I don't know why."
- "The fix didn't work."
- "It works locally but not in prod."
- "Let's debug this properly."

## Non-goals

- This skill does not replace implementation planning.
- This skill does not require heavyweight process for trivial edits.
- This skill is about root cause, not about writing the prettiest postmortem.
