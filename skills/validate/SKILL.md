---
name: validate
description: Run comprehensive repository validation when explicitly requested or required by the repository's completion gate. Skip for a narrow confidence check that does not require the full suite.
---

# Run repository validation

1. Find the actual validation contract in applicable instructions, package scripts, and CI. Identify the required commands and prerequisites for this change; do not invent lint, build, test, or end-to-end scripts.
2. Use the repository's umbrella command when it covers those checks, with pnpm for JavaScript packages. Add required checks it does not cover. Avoid running the same layer both directly and through a wrapper.
3. Run checks in dependency order. Independent checks may run concurrently when they do not compete for shared services or outputs. A prerequisite failure blocks its dependents; continue independent checks when useful for the requested validation.
4. For failures, identify the command and actionable cause. Fix within the authorized scope, then rerun the affected checks and any dependent checks whose evidence is invalidated.
5. Report passed, failed, and unavailable checks, including any required coverage still missing.

Completed checks can satisfy the gate while the relevant source and environment remain unchanged. An explicit request to rerun takes precedence. Do not install unrelated tooling, deploy, reset databases, or change production as a validation side effect; use an appropriate local or already authorized environment.
