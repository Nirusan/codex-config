---
name: completion-verification
description: Check that evidence supports a requested readiness, fix, delivery, or completion claim. Use when the claim needs review; skip repeating checks already sufficient for the unchanged result.
---

# Match the claim to the evidence

1. State what is being claimed and the relevant acceptance conditions. Identify the evidence needed for that claim, including repository-required checks.
2. Inspect existing results and their scope: command, outcome, source state, environment, and timing where material. Evidence must cover the latest relevant changes. Reuse it when those conditions are unchanged; rerun when requested, after a relevant change, or when a failure or unresolved concern warrants it.
3. Obtain only missing proof. Use the repository's actual commands; avoid rerunning layers already covered by an umbrella command. Do not weaken a required check because a smaller one passed.
4. Review the scoped diff or artifact for unintended changes. Separate passed, failed, and unverified conditions in the completion report.

Match evidence to the runtime and effect:
- Unit tests and replays establish their exercised behavior, not physical-device or production behavior.
- Review web UI in its browser runtime and native UI through relevant native tooling. If a needed visual or device check is unavailable, state the gap.
- A local migration check establishes only that environment. Apply migrations only to an appropriate disposable environment or an already authorized target.
- Source, build, publication, routing, installation, and observed user behavior are separate delivery states. Verify the state being claimed.
- For a commit, push, or merge claim, inspect the intended changes and target; check CI or remote state when the claim depends on it.

Verification does not expand authorization. Perform already authorized effects within their exact scope; do not publish, mutate production, or contact others merely to obtain proof. Report limitations directly without labeling unverified work as passed.
