---
name: refresh-context
description: Recover missing project state for a handoff, resumption, or status question when earlier assumptions may be stale. Skip when the task's relevant context is already available.
---

# Recover project context

1. Identify the missing decision or state: what the user wants to resume, verify, or choose.
2. Follow applicable repository instructions. Read the nearest current source of truth for that question, such as a decision, task record, relevant README section, or changed source. Search headings or identifiers before opening large documents.
3. Check facts that may have drifted when relevant: working tree changes, task status, current implementation, or the referenced artifact. Treat chat and memory as pointers; resolve conflicts using the repository's stated authority order and current evidence.
4. Stop reading when the requested decision has enough support. Do not load every planning document, reconstruct unrelated history, or run validation merely to recover context.
5. Briefly state the verified state, the remaining uncertainty, and the next action if one is requested. Distinguish recorded plans from implemented, tested, or delivered behavior.

A missing tracker does not require creating a plan. A deployment or live service question may need separate current evidence; local source alone cannot establish remote state. Reuse context already present instead of asking the user to repeat it.
