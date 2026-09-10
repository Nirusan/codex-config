# Utility Writing

Use this after the anti-slop pass.

The goal is not just to make text sound human. The goal is to make it carry more usable information per sentence.

## Core idea

A strong sentence should be useful even when read alone.

That usually means:
- it names the subject clearly
- it states the relationship directly
- it preserves the relevant condition or constraint
- it avoids vague references like "this", "that", or "it" when clarity matters

## What to optimize for

### 1. Self-contained sentences

Weak:
- This changed everything.
- It worked much better than expected.

Better:
- Anthropic blocking Claude Pro and Max for OpenClaw changed the economics of many low-cost setups.
- OpenAI performed better than expected in OpenClaw once the prompts and tool config were cleaned up.

### 2. Explicit relationships

Weak:
- OpenClaw, Anthropic, and pricing all became a problem.

Better:
- Anthropic’s policy change broke a cheap OpenClaw setup that depended on Claude Pro or Max.

### 3. Conditions inline

Weak:
- OpenAI still works well.

Better:
- OpenAI still works well in OpenClaw when the model choice, prompts, and tool settings are configured correctly.

### 4. Concrete comparisons

Weak:
- It was much better.

Better:
- GPT-5.4 gave more stable tool behavior than the previous setup, but needed tighter prompting.

### 5. Named actors

Weak:
- A decision was made and the setup stopped working.

Better:
- Anthropic changed the rules, and that made the previous OpenClaw setup non-viable.

## Default rewrite moves

- replace pronouns with the entity when clarity improves
- replace grouped nouns with an actual relationship
- add the missing condition, audience, or tradeoff
- replace generic praise with the mechanism behind it
- keep the sentence quotable

## Quotable anchor sentence

When the format allows it, give the text one sentence that can survive on its own.

Examples:
- Most people do not need an AI agent. They need one specific job automated.
- The hard part of OpenClaw is not installing it. The hard part is knowing what job to give it.
- A setup is only useful if the person using it knows what task it owns.

## What not to do

- Do not turn everything into a slogan.
- Do not make every sentence maximally dense.
- Do not remove all rhythm or voice.
- Do not expand text just to add explicitness.

Utility matters, but pace still matters.

## Good test

Ask:
- if this sentence were screenshotted alone, would it still make sense?
- does it name who did what to whom?
- does it preserve the condition that makes the claim true?
- is it more useful now than before?
