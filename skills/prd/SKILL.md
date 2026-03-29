---
name: prd
description: Use when the user wants to turn a product idea or feature brief into concrete requirements. Produces a Product Requirements Document with scope, user stories, acceptance criteria, priorities, constraints, and open questions. Do not use for architecture design, debugging, or implementation execution.
---

# Product Requirements Document

Use this skill when the user wants real requirements, not just ideation.

## Use when

- the problem and solution are directionally known
- the user wants to define MVP scope
- you need user stories and acceptance criteria before implementation
- a feature needs its own requirements document

## Don't use when

- the idea is still too vague and needs discovery first
- the main need is technical architecture
- the task is already implementation-ready and only needs a build plan

## Goal

Write a PRD that is specific enough to guide architecture and implementation without pretending every detail is settled.

## Workflow

1. Read relevant context if it exists:
   - `AGENTS.md`
   - a brief (`memory-bank/brief.md`, `docs/brief.md`, or equivalent)
   - an existing PRD if you are refining rather than starting fresh
   - existing product docs that define constraints or terminology
2. Confirm whether the PRD is:
   - for the main product
   - for a specific feature
3. Resolve the output path by following the repo's existing documentation structure.
4. Ask targeted clarification questions only when they materially change scope or requirements.
5. Produce the PRD with explicit non-goals and acceptance criteria.

## Output path

Prefer this order:

1. `memory-bank/features/<feature-name>/prd.md` for feature-specific work when that structure already exists
2. `memory-bank/prd.md` for a main product PRD when `memory-bank/` exists
3. `docs/features/<feature-name>/prd.md` if the repo uses `docs/` instead
4. `docs/prd.md` otherwise

## PRD structure

```md
# PRD: {Name}

## Overview
{One-paragraph summary}

## Goals
- Primary: {main objective}
- Secondary: {supporting objective}

## Non-Goals
- {explicitly out of scope}

## Target Users
- {user type}: {context and need}

## Core User Stories
1. As a {user}, I want to {action} so that {benefit}
   - Acceptance Criteria:
     - [ ] {criterion}
     - [ ] {criterion}

## Functional Requirements
| ID | Requirement | Priority | Notes |
|----|-------------|----------|-------|
| FR-1 | {requirement} | Must | {notes} |

## Non-Functional Requirements
| Category | Requirement | Target |
|----------|-------------|--------|
| Performance | {requirement} | {target} |

## Dependencies
- {external system, internal prerequisite, or assumption}

## Risks and Open Questions
- {risk or unresolved point}

## Success Metrics
- {metric}: {target}
```

## Writing rules

- Prefer testable requirements over aspirational language.
- Separate must-have behavior from future ideas.
- If something is unknown, put it in open questions rather than faking precision.
- Reuse real product labels and terminology when they already exist.

## Suggested next step

Once the PRD is solid, the next steps are usually:

- `$tech-stack`
- `$implementation-plan`
