---
name: tech-stack
description: Use when the user wants to define or refine the technical stack and architecture for a product or feature. Produces a concrete architecture document that maps requirements to implementation choices, constraints, integrations, and risks. Do not use for product discovery, UI art direction, or direct feature implementation.
---

# Tech Stack

Use this skill when the main question is architectural, not product or visual.

## Use when

- the user wants help choosing stack components
- architecture tradeoffs need to be written down
- the project needs an implementation-facing technical reference
- a feature introduces meaningful new infra, security, or data concerns

## Don't use when

- the main task is still product discovery
- the answer should be a PRD rather than technical design
- the user already knows the stack and wants implementation only

## Goal

Produce a practical architecture document that reflects real constraints and repo conventions.

## Workflow

1. Read the relevant context:
   - `AGENTS.md`
   - product docs such as a brief or PRD
   - `package.json` and the existing codebase if this is a brownfield project
2. Determine whether the project is:
   - greenfield
   - brownfield with an existing stack to preserve
3. Identify the real constraints:
   - hosting
   - cost
   - performance
   - auth/security
   - data model
   - team familiarity
   - integrations
4. Prefer compatibility with the existing repo when working in brownfield mode.
5. Only present multiple options when the tradeoff is real.
6. Produce a single recommended architecture with rationale.

## Output path

Prefer this order:

1. `memory-bank/tech-stack.md` if `memory-bank/` exists
2. `docs/tech-stack.md`

## Suggested structure

```md
# Tech Stack

## Overview
{One-paragraph rationale}

## Product shape
{Greenfield or brownfield, main assumptions}

## Frontend
| Layer | Choice | Rationale |
|-------|--------|-----------|

## Backend
| Layer | Choice | Rationale |
|-------|--------|-----------|

## Data and integrations
- {database}
- {storage}
- {queues, cache, webhooks, realtime, etc.}

## Infrastructure
| Layer | Choice | Rationale |
|-------|--------|-----------|

## Security and permissions
- {auth approach}
- {authorization approach}
- {sensitive boundaries}

## Architecture decisions
### ADR-1: {Decision}
- Context:
- Decision:
- Alternatives considered:
- Consequences:

## Risks and follow-ups
- {risk}
```

## Writing rules

- Reflect the existing repo before proposing new tools.
- Avoid stack tourism: every choice should have a reason.
- Distinguish hard requirements from defaults and preferences.
- Call out risky assumptions explicitly.

## Suggested next step

Once the stack is clear, the next step is usually `$implementation-plan`.
