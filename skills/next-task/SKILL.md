---
name: next-task
description: Use when the user asks what to work on next, wants the next incomplete story from a plan, or needs a concise status-based recommendation. Reads the current plan and progress tracker, identifies the next actionable item, and explains any blockers or missing prerequisites. Do not use when no plan exists and the user actually needs planning first.
---

# Next Task

Use this skill to answer "what should we do next?" from actual project state.

## Use when

- the user asks for the next task
- a plan exists and the next unfinished story should be identified
- the user wants a quick status-based recommendation

## Don't use when

- there is no plan or tracking doc and the user really needs one
- the task is brainstorming rather than execution sequencing

## Workflow

1. Read the best available plan and progress files.
2. Follow the repo's existing planning structure rather than inventing a new one.
3. Compare:
   - remaining stories
   - current story
   - explicit blockers or dependencies
4. Identify the next actionable task, not just the first unchecked line.
5. If no plan exists, say so and recommend the appropriate planning step instead.

## Path resolution

Prefer this order:

1. feature-level `memory-bank/features/<feature>/plan.md` + `progress.md` when clearly in scope
2. `memory-bank/plan.md` + `memory-bank/progress.md`
3. `docs/implementation-plan.md` + `docs/progress.md`
4. the closest equivalent tracked docs already used by the repo

## Output format

Return a concise status block with:

- current phase or area if known
- what is already done
- the next story or task
- why that is the next task
- any blocker or prerequisite

## If everything is done

Say so clearly and recommend the next sensible move, such as:

- validation
- documentation cleanup
- a new feature plan

## If the plan is unclear

Do not guess too hard. State the ambiguity and suggest:

- `$implementation-plan`
- or a direct clarification question if that is the shortest path
