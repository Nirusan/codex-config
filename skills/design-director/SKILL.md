---
name: design-director
description: Use when the user wants help steering AI-generated frontend design, defining a visual direction, writing anti-goals, preparing a Gemini/OpenAI frontend brief, or reducing iteration churn on UI work. Guides from vague taste to clear constraints, references, validation steps, and durable design rules.
---

# Design Director

Use this skill when the design problem is not "write some UI" but "help us direct the UI well."

This skill is about art direction and generation quality control. It helps turn fuzzy feedback into a repeatable frontend brief before asking a model to generate or modify visuals.

## What This Skill Does

- Translates taste-level feedback into explicit design rules
- Prevents derivative or generic AI frontend output
- Builds a structured brief for Gemini, GPT, or another frontend model
- Chooses whether the team needs vibe exploration, a full generation, or a small design edit
- Converts review feedback into durable rules so the same problem does not repeat

## When To Use It

Use this skill when the user asks for any of the following:

- "Help us define the design direction"
- "We keep needing multiple tries with Gemini"
- "Make a better frontend prompt"
- "How should we steer the model for design?"
- "This feels too generic / too close to brand X / too aggressive / too flat"
- "Let's create a reusable design workflow"

Do not use this skill for:

- pure logic changes
- text-only edits
- data wiring
- non-visual bug fixes

## Core Principle

The goal is not to get the model to imitate a reference. The goal is to give the model enough constraints that it can produce something specific, attractive, and usable.

Use this framing:

- `brand-compatible, not brand-derivative`
- `specific, not generic`
- `usable first, expressive second`
- `real content, not placeholders`

## Workflow

Follow this order.

### 1. Read The Local Rules First

Before proposing any design direction:

1. Read `AGENTS.md` in the repo root if present.
2. Read `design-system.md` in the repo root if present.
3. Read the real product copy, labels, data values, and page structure that the UI must render.

If the project already has a design system, preserve it unless the user explicitly wants a redesign.

### 2. Define The Design Problem

Write a short diagnosis in plain language:

- What is wrong with the current direction?
- What must stay?
- What must change?
- What is the emotional job of the screen?

Do not jump into code or styling proposals before naming the actual problem.

### 3. Produce A Design Brief

Create a brief with these exact sections:

1. `Visual Thesis`
One sentence describing the intended feel.

2. `Narrative Structure`
What each section of the page needs to do in sequence.

3. `Must Keep`
Existing strengths or constraints to preserve.

4. `Must Change`
Specific weaknesses to fix.

5. `Brand Relationship`
How close or far the design should be from any reference brand.

6. `Anti-Goals`
Explicit things the model must not do.

7. `Real Content Inventory`
Titles, labels, buttons, states, data values, locales, and any business-specific text.

8. `Validation Plan`
How the result will be checked in browser and what success looks like.

### 4. Choose The Right Generation Mode

Pick exactly one of these:

- `Vibes exploration`
Use when the project lacks a design system or the team is still choosing a direction.

- `Full generation`
Use when the direction is approved and a new screen or section needs to be created.

- `Focused design edit`
Use when the structure is good and only one visual issue should change.

- `Snippet insertion`
Use when adding a small UI region without rewriting the whole file.

Do not ask the model for a full rewrite if the real need is a narrow visual adjustment.

### 5. Apply Frontend Guardrails

Always include these constraints in the brief when relevant:

- Do not invent product copy, data, features, or branding.
- Do not clone the layout or hero of a reference brand.
- Do not prioritize resemblance over beauty or readability.
- Do not add decorative complexity without a job.
- Do not hide hierarchy behind glow, tilt, noise, or heavy effects.
- Do not make every section visually loud.
- Reserve the strongest visual tension for the most important moments.

### 6. Review In Browser

After generation, review the actual UI:

- desktop
- mobile
- all supported locales
- empty / loading / result states if applicable

Check these in order:

1. Readability
2. Hierarchy
3. Brand fit
4. Interaction clarity
5. Emotional tone
6. Visual uniqueness

### 7. Turn Feedback Into Durable Rules

If the user says things like:

- "too close to X"
- "too aggressive"
- "too generic"
- "less tilted"
- "calmer but still premium"

Do not just retry with softer wording. Convert that into explicit future rules in the project docs or design system.

Examples:

- `No global tilt on primary reading surfaces`
- `Use warning color only for risk states, not as the base theme`
- `Reference brand can influence palette but not layout`

## Anti-Patterns

Avoid these common failure modes:

- vague prompts like "make it nicer" or "more premium"
- using a reference brand as a direct composition template
- providing style wishes without real content
- asking for final code before approving a direction
- letting the model choose between multiple competing visual ideas at once
- accepting a result because it is closer to the reference even if it is uglier

## Output Format

When using this skill, your ideal output is usually one of these:

- a short design diagnosis plus a proposed direction
- a structured design brief ready for Gemini/OpenAI
- a small list of tightly scoped visual directions to choose from
- a set of durable anti-rules to add to project docs

Prefer compact, operational outputs over long theory.

## References

Open only what you need:

- Reusable brief template: `references/brief-template.md`
