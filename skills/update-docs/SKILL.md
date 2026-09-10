---
name: update-docs
description: Update durable repository documentation when a requested change makes documented behavior, setup, interfaces, or decisions inaccurate. Skip one-off implementation details and changes with no documentation impact.
---

# Keep existing documentation accurate

1. Identify the durable fact that changed and the existing document that owns it. Confirm the fact in the implementation, configuration, or recorded decision; do not turn assumptions into documentation.
2. Update the relevant section in place. Preserve the repository's authority order and link to an existing source instead of copying it into several files.
3. Document behavior, constraints, setup steps, or interfaces that a future reader needs. Avoid narrating the coding session, duplicating obvious code, or inventing new documents to satisfy a workflow.
4. Put rules in AGENTS.md only when they are stable, broadly useful to agents, and not already supplied elsewhere. A single incident rarely justifies a universal instruction.
5. Check the changed text, referenced paths, and commands against current evidence. If no durable documentation change is needed, leave the files untouched.

Track completion in the existing progress record only when that status also changed. Write internal technical documentation in English unless the user or document's audience requires otherwise. Repository documentation work does not itself authorize changing persistent assistant memories or publishing externally.
