---
name: responsive-frontend-designs
description: Use when the user wants to build or refine a responsive UI from screenshots, mockups, or visual references. Reuse the repo's existing design system and frontend patterns, treat the references as the visual source of truth, and validate the implementation in a real browser with Playwright.
---

# Responsive Front-End Designs

Use this skill when a user provides screenshots, design references, or a concise visual brief and wants the implementation to match responsively.

## Core workflow

1. Gather the screenshots, states, and notes that define the intended UI.
2. Identify the repo's real design system, tokens, primitives, and routing/data patterns.
3. Implement the UI using the repo's existing patterns instead of inventing a parallel system.
4. Check the result in a live browser at multiple breakpoints.
5. Iterate until the layout, hierarchy, and behavior are meaningfully closer to the references.

## Source of truth

- Treat screenshots and visual references as the target for spacing, hierarchy, density, and interaction cues.
- When details are ambiguous, choose the simplest implementation that still fits the overall direction.
- Preserve the repo's actual component and token system even when the reference uses a different style vocabulary.

## Recommended tools and skills

- Use `$playwright` to inspect the implementation in a real browser, compare desktop and mobile layouts, and iterate visually.
- Use local project docs, `AGENTS.md`, and existing UI files before inventing new patterns.
- Use Gemini frontend tools only if the repo rules require them for the specific UI task.

## Implementation guidance

- Reuse canonical buttons, inputs, cards, typography, spacing tokens, icons, and utilities from the repo.
- Match responsive behavior on desktop and mobile, not just the default viewport.
- Respect the repo's routing, state, and data-fetch patterns.
- Prefer minimal, targeted layout adjustments over rewriting established UI patterns.
- If the task includes multiple states, implement the most important states first, then refine.

## Validation expectations

- Compare the finished UI against the provided references for both look and behavior.
- Check at least one desktop width and one mobile width when responsiveness matters.
- Note any important assumptions briefly if the reference leaves room for interpretation.
