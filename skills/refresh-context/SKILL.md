---
name: refresh-context
description: Re-read the project's key docs to recover working context at the start of a session, after a break, or when the user asks for the current state. Reads AGENTS, planning docs, progress, and other high-signal project files, then summarizes the active constraints, current status, and likely next move.
---

# Refresh Context

Use this skill to rebuild working context without rereading the entire repo blindly.

## Use when

- starting a new session in an existing project
- resuming after a break
- the user asks "where are we?", "what's the current state?", or equivalent

## Workflow

1. Read `AGENTS.md` first if present.
2. Read the highest-signal project docs next, typically:
   - brief / PRD / tech-stack
   - plan / progress
   - design-system if relevant
   - schema or other key technical docs only when they matter
3. Prefer the repo's real planning structure:
   - `memory-bank/`
   - or `docs/`
   - or root planning docs if that is what the repo uses
4. Ignore low-signal or stale brainstorming debris unless it is still actively relevant.
5. Summarize:
   - stack and conventions
   - current work status
   - important open risks or constraints
   - likely next action

## Good summary structure

```md
## Context Loaded

**Project**
- {name or repo}

**Key conventions**
- {important rule}

**Current status**
- {where work stands}

**Open constraints**
- {important blocker, assumption, or risk}

**Suggested next step**
- {next likely move}
```

## Rules

- Read selectively, not exhaustively.
- Prefer current implementation docs over old brainstorm notes.
- If there are conflicting docs, call that out instead of flattening the disagreement.
