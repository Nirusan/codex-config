---
name: implementation-plan
description: Use when requirements are concrete enough to break work into implementable stories. Produces a phased implementation plan and a matching progress tracker, with dependencies, likely files, acceptance criteria, and verification steps. Do not use for vague ideation, pure architecture work, or direct coding without planning.
---

# Implementation Plan

Use this skill to turn requirements into a buildable sequence.

## Use when

- the user wants a phased implementation plan
- the PRD or technical context is strong enough to define stories
- the next question is "how should we build this?"

## Don't use when

- the feature is still vague
- the main need is product discovery or architecture choice
- the user explicitly wants immediate implementation without a formal plan

## Goal

Break the work into small, dependency-aware stories that can be executed with confidence.

## Workflow

1. Read the best available context:
   - PRD
   - tech-stack or equivalent architecture notes
   - brief if requirements are still light
   - `AGENTS.md`
2. Determine whether the plan is:
   - for the main project
   - for a specific feature
3. Follow the repo's existing documentation layout if one exists.
4. If requirements are incomplete, state the assumptions clearly instead of blocking on perfection.
5. Write:
   - a `plan.md`
   - a `progress.md`

## Output path

Prefer this order:

1. `memory-bank/features/<feature-name>/plan.md` and `progress.md` if that structure exists
2. `memory-bank/plan.md` and `memory-bank/progress.md`
3. `docs/implementation-plan.md` and `docs/progress.md`

## Plan expectations

- group stories by dependency, not by team fantasy
- keep stories small enough for one focused implementation session
- include likely files or system areas affected
- include verification notes
- call out blockers and sequencing risks

## Plan structure

```md
# Implementation Plan: {Name}

## Overview
{What is being built and how}

## Assumptions
- {assumption}

## Phases
### Phase 1: Foundation
| # | Story | Goal | Complexity |
|---|-------|------|------------|

## Story details
### Story 1: {Title}
**Goal**: {what this enables}

**Tasks**
- [ ] {task}
- [ ] {task}

**Acceptance Criteria**
- [ ] {criterion}

**Likely files / systems**
- `path/to/file`

**Verification**
- {what to check}

**Dependencies**
- {if any}
```

## Progress structure

```md
# Progress: {Name}

## Status
Not started

## Current Story
None

## Completed
(none yet)

## In Progress
(none yet)

## Remaining
- [ ] Story 1: {title}
- [ ] Story 2: {title}

## Notes
- {important decisions, blockers, or assumptions}
```

## Writing rules

- Prefer realistic implementation order over pretty phase names.
- Separate implementation tasks from manual validation tasks.
- Do not fake certainty about files or estimates.
- Keep the first version lean; refinement can happen later.

## Suggested next step

After creating the plan, the natural next skills are:

- `$next-task`
- `$implement`
