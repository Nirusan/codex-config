---
name: stop-slop
description: Remove AI writing patterns from prose and rebuild it into human, direct, high-utility writing. Use when drafting or editing text that should sound natural, specific, and non-synthetic, especially for Reddit posts/comments, tweets, essays, landing pages, and opinionated social content.
metadata:
  short-description: Rewrite synthetic prose into direct, useful human writing
---

# Stop Slop

Turn synthetic prose into human prose.

This skill is not just an AI-tell remover. It has two jobs:
1. remove synthetic writing patterns
2. rebuild the text so it carries more concrete meaning per sentence

Use it to make text sound:
- more human
- more direct
- more specific
- more useful to quote, retrieve, or reuse

## Workflow

1) Draft or inspect the text in context.
2) Pick the stop-slop intensity.
3) Run the anti-slop pass.
4) Rebuild for utility.
5) Do a final voice check.

## Intensity levels

### Light pass
Use when the draft is already decent and just needs cleanup.

Goal:
- remove obvious AI tells
- keep most of the original structure
- avoid over-rewriting

Apply:
- cut throat-clearing
- cut filler and adverbs
- cut fake emphasis
- remove em dashes
- simplify a few inflated phrases

### Strong pass
Default mode. Use when the user says "unslop" with no qualifier.

Goal:
- make the text sound human, direct, and specific
- remove structural AI patterns, not just vocabulary

Apply:
- everything in Light pass
- ban significance inflation
- ban superficial analysis
- ban negative parallelisms
- ban vague attribution
- ban inflated verbs
- ban challenge/future-outlook filler
- collapse AI-vocabulary clusters
- replace generic praise with specifics

### Brutal pass
Use when the user wants a ruthless rewrite, or when the draft is deeply synthetic.

Goal:
- maximize clarity, density, and specificity
- sacrifice smooth AI elegance if needed

Apply:
- everything in Strong pass
- cut any sentence that adds framing but no payload
- rewrite smooth-but-vague lines into concrete lines
- prefer repeated simple nouns over elegant variation
- remove listicle energy
- compress 2 to 3 weak sentences into 1 strong one
- force every abstract claim to earn its place

## Anti-slop pass

Default moves:
- Cut throat-clearing, emphasis crutches, meta-commentary, and jargon.
- Break formulaic structures like binary contrasts, negative listing, and rhetorical setups.
- Cut tagline fragments and contrast closers like "X, not Y." when they act as style, not information.
- Rewrite blog intros and subheads that posture, tease, or brand the paragraph instead of stating the point.
- Rewrite passive voice into active voice.
- Name the actor.
- Avoid fake agency like "the data tells us".
- Replace broad claims with specific claims.
- Replace prestige language with facts.

Read these references as needed:
- Phrases to remove: `references/phrases.md`
- Structures to avoid: `references/structures.md`
- Before/after examples: `references/examples.md`
- Utility-first rewrite patterns: `references/utility-writing.md`
- Wikipedia-derived AI writing patterns: `references/wikipedia-ai-signs.md`

When editing blog posts, landing pages, or social copy, pay extra attention to:
- opener sentences that frame the framing instead of giving the point
- subheads that sound like taglines or verdicts
- standalone contrast fragments
- “this is where / this is why / this is not” setups

If the user wants a stricter anti-slop pass, read `references/wikipedia-ai-signs.md` too and ban the pattern families listed there, especially significance inflation, broader-trend padding, abstract praise, generic “this highlights/underscores” glue, AI-vocabulary clusters, inflated verbs, vague attribution, and school-essay challenge/future-outlook filler.

## Rebuild for utility

After removing slop, do not stop at cleanup. Rebuild the text so each sentence carries clearer information.

Default moves:
- Make sentences more self-contained.
- Resolve weak pronouns when possible.
- Name entities explicitly.
- State relationships directly.
- Keep conditions inline.
- Prefer concrete comparisons over generic praise.
- Add at least one quoteable anchor sentence when the format allows it.

Examples:
- weak: "OpenAI still works well"
- better: "OpenAI still gives solid results in OpenClaw when the prompts, model choice, and tool setup are configured correctly"

- weak: "That changed everything"
- better: "Anthropic no longer allowed Claude Pro or Max to be used with OpenClaw, so users had to retest models, costs, and configs"

The goal is not only to sound human. The goal is to make the text easier to understand, quote, and reuse.

## Final voice check

Before final output, check:
- Does this sound like a person with a point, not a model with a tone?
- Is the text specific enough to be falsifiable?
- Did any sentence survive only because it sounded smooth?
- Can any abstract line be replaced with a fact, number, actor, or example?
- Did I keep the writer’s intent, or overwrite it with my own preferences?

## Quick checklist

- No adverbs doing fake work.
- No vague importance claims ("the implications are significant").
- No inflated significance language ("pivotal", "vital", "lasting impact", "broader trend") unless proven with specifics.
- No Wh- sentence starters as a habit.
- No em dash characters. Use commas or periods.
- No tagline fragments like "Tradeoffs, not hype." or "Signals, not noise."
- No intro or subhead that sounds like a mini-manifesto when a plain sentence would do.
- No AI-vocabulary clusters, inflated verb choices, or vague expert-attribution filler.
- More specifics, fewer abstractions.
- At least one sentence should stand on its own without leaning on surrounding context.
