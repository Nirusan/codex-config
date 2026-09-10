---
name: next-task
description: Choose the next useful task from an existing goal, plan, or work queue when the user asks what to do next. Skip when the user has already selected the work or only asks for status.
---

# Choose the next task

1. Read the relevant goal and current queue or tracker, if one exists. Follow the repository's stated source-of-truth order; do not load unrelated planning documents.
2. Check enough implementation and working tree evidence to avoid recommending completed work or colliding with active changes.
3. Select an actionable task using stated priorities, dependencies, user impact, and blockers. The first unchecked item is not necessarily ready. Explain any departure from the recorded order.
4. Give a concrete next task, why it comes next, its completion condition, and any blocking dependency. Do not present unverified tracker status as current fact.

If no plan exists, recommend a bounded next step from the user's goal and available evidence; do not require a new planning workflow. Ask for missing direction only when it materially changes the choice.

Choosing a task does not authorize executing it. Continue into implementation when the user requested that work, such as "take the next task and implement it"; otherwise return the recommendation.
