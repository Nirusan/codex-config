---
name: implement
description: Carry a concrete feature or bug fix through implementation and relevant verification. Use for requested code changes; skip for status-only questions, requirements exploration, or Git-only operations.
---

# Implement the requested change

1. Establish the requested behavior and acceptance conditions from the task and applicable repository guidance. Inspect the affected source and relevant tests; read planning or design documents only when they constrain this change. Do not select a different task because a tracker exists.
2. Check the working tree before editing. Preserve unrelated changes; use isolation when overlapping work or risk warrants it. For a bug, obtain a concrete reproduction or evidence of the failing path before choosing a fix.
3. Make the smallest coherent change that completes the request. Preserve existing domain invariants, interfaces, and product conventions. Investigate surprising failures before stacking speculative fixes.
4. Verify the changed behavior and complete repository-required checks. Use the repository's real commands, with pnpm for JavaScript packages. A wrapper that already runs a check does not require that check again. Reuse successful evidence for unchanged code and conditions unless a rerun is requested or a new concern warrants one.
5. Update existing documentation or task status only when the change makes them inaccurate. Keep implementation, testing, delivery, and remaining manual acceptance distinct where relevant.
6. Report the resulting behavior, relevant proof, and remaining limits. Complete all authorized work needed for the requested outcome.

No companion skill is a mandatory step. Consult focused guidance when the problem requires it. Implementation alone does not authorize publishing, deployment, production data changes, or messages to others; carry forward any existing authorization for the exact action and target without asking again.
