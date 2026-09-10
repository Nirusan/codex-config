---
name: validate-quick
description: Obtain a fast, bounded confidence check for a small change or an explicit quick validation request. Skip when full validation is requested or the repository requires a broader gate.
---

# Check the changed behavior quickly

1. Inspect the affected diff and available repository scripts. Choose the smallest check that meaningfully covers the change: a focused regression test, type check, lint, or build as appropriate. Lint alone does not prove a behavior fix.
2. Reuse a relevant successful check on unchanged code and conditions; run it again when requested or when new changes or concerns require it. Use pnpm for JavaScript package scripts.
3. If it fails, diagnose the specific failure. Expand checking only when the failure, affected dependencies, or repository requirements justify it.
4. Report the command, result, scope covered, and material checks still outstanding.

A quick pass is limited evidence. It does not replace repository-required checks or establish full release readiness. Do not chain another validation or completion skill just to repeat the same proof.
