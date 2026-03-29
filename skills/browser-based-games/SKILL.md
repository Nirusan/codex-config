---
name: browser-based-games
description: Use when the user wants to plan, build, test, or iterate on a browser-based game. Start by defining a concrete PLAN.md, then implement and tune the game in a live browser with Playwright, generate assets with Imagegen when needed, and check official OpenAI docs before adding OpenAI-powered features.
---

# Browser-Based Games

Use this skill when a user wants to create or improve a browser game in a repo.

## Core workflow

1. Start with a concrete `PLAN.md` before scaffolding major game code.
2. Implement the game in milestone order instead of trying to ship everything at once.
3. Test the real build in a live browser and iterate on controls, timing, layout, and feel.
4. Keep lightweight logs of progress and decisions under `.logs/` when the task is substantial.
5. Save reusable image prompts under `.prompts/` when generating batches of visual assets.

## Plan first

Before coding major gameplay systems, write or update `PLAN.md` with at least:

- player goal
- core gameplay loop
- inputs and controls
- win and fail states
- progression or difficulty
- visual direction
- stack and hosting assumptions
- milestone order

If the user brief is vague, tighten the spec before implementation.

## Recommended tools and skills

- Use `$playwright` to open the real build, play the game, inspect UI states, and iterate on gameplay feel.
- Use `$imagegen` for sprites, backgrounds, concept art, UI assets, and prompt reuse.
- Use `$openai-docs` before wiring OpenAI-powered mechanics or APIs.
- Use Context7 when the user chooses a rendering/game framework and current framework docs matter.

## Implementation guidance

- Prefer a practical browser game stack such as Next.js plus Phaser or PixiJS unless the repo already dictates something else.
- Build the shell, loop, controls, and feedback first; add polish after the game is playable.
- Keep gameplay parameters easy to tune.
- Validate frequently in the browser instead of relying only on static code review.
- When visuals are generated, keep style prompts consistent so later asset batches match.

## Delivery expectations

- The game should be playable in the browser, not just scaffolded.
- Controls and UI should be tested against the real running build.
- Assumptions and milestone changes should be recorded briefly when they affect implementation.
