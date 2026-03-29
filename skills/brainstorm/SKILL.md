---
name: brainstorm
description: Use when the user wants to explore or sharpen a product idea before writing requirements or code. Helps turn a vague concept into a concrete brief by clarifying the problem, target users, alternatives, differentiators, success criteria, and open questions. Do not use for implementation, debugging, or finalized requirements work.
---

# Brainstorm

Use this skill for product discovery before PRDs or implementation plans.

## Use when

- the idea is still fuzzy
- the user wants to explore options before committing
- the problem, user, or differentiator is not fully clear yet
- you need a short written brief that future planning can build on

## Don't use when

- the user already has concrete requirements and wants a PRD
- the task is implementation or debugging
- the request is only to rewrite existing docs without discovery

## Goal

Turn a rough concept into a brief that is specific enough for the next planning step.

## Workflow

1. Read the local context if it exists:
   - `AGENTS.md`
   - `memory-bank/brief.md`, `memory-bank/prd.md`
   - or equivalent files in `docs/` or the repo root
2. Summarize the current understanding in plain language.
3. Ask only the highest-value questions needed to remove ambiguity. Prioritize:
   - the problem
   - the user
   - current alternatives
   - why this deserves to exist
   - what success looks like
4. When the user already gave enough information, synthesize instead of over-questioning.
5. Produce or update a concise brief.

## Output path

Prefer this order:

1. `memory-bank/brief.md` if `memory-bank/` exists
2. `docs/brief.md` if `docs/` exists
3. `brief.md` at the repo root only if the project has no better documentation home

## Brief structure

Use this structure unless the repo already has an established template:

```md
# Product Brief: {Name}

## Problem Statement
{What is broken or missing today?}

## Target User
{Who has the problem and in what context?}

## Current Alternatives
{What they do today and why it is insufficient}

## Proposed Solution
{High-level product concept}

## Key Differentiator
{Why this is worth building}

## Success Criteria
{How we will know this is working}

## Open Questions
{What still needs to be decided}

## Out of Scope
{What this brief is not trying to solve}
```

## Output style

- Be concrete, not visionary for its own sake.
- Prefer specific tradeoffs over broad ambition.
- Keep the brief short enough to read quickly.

## Suggested next step

After the brief is solid, the natural next steps are usually:

- `$prd`
- `$tech-stack`

depending on whether the user wants requirements first or architecture first.
