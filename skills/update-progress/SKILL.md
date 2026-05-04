---
name: update-progress
description: Use after meaningful implementation work when the project keeps a plan and progress tracker. Updates the progress file and, when appropriate, the implementation plan to reflect what was actually completed, what is still in progress, and any important blockers or decisions. Do not use when no tracked planning structure exists.
---

# Update Progress

Use this skill to keep planning artifacts honest after work is completed.

## Use when

- a planned story or task was completed
- tracked work moved from remaining to in progress or done
- important implementation notes or blockers should be recorded

## Don't use when

- the repo has no planning or progress files
- nothing meaningful changed
- the user only wants a verbal summary, not doc updates

## Workflow

1. Find the repo's actual tracking files.
   Prefer:
   - feature-level `memory-bank/features/<feature>/plan.md` and `progress.md`
   - `memory-bank/plan.md` and `memory-bank/progress.md`
   - `docs/implementation-plan.md` and `docs/progress.md`
2. Read the current plan and progress state.
3. Gather evidence of the work actually completed:
   - `git diff` or staged diff
   - files modified
   - tests, validation, or repro evidence when relevant
   - explicit decisions or blockers from the current task
4. Compare the tracker to the evidence, not just the conversation.
5. Update the progress file conservatively:
   - move completed stories or tasks to the right section
   - update the current story if needed
   - add important notes, blockers, or assumptions
6. Update the plan only when the change is factual and justified.
   - mark implementation tasks done if the code now exists
   - do not mark manual validation steps done without evidence
7. Report what changed.

## Rules

- Reflect reality, not optimism.
- Do not mark work complete without concrete evidence.
- If you are unsure which story was completed, say so instead of guessing.
- Do not create a fake planning system just to satisfy the skill.
- If a progress file is missing but the repo clearly tracks plans, create it only if that fits the repo's established structure.

## Output

Summarize:

- which files were updated
- what story or task moved state
- what evidence justified the update
- what remains next
