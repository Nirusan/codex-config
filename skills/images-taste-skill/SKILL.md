---
name: image-taste-frontend
description: Turn supplied or requested design images into a responsive website when image-led art direction is explicitly chosen.
---

# Image-led website implementation

Use an existing reference when supplied. Generate a reference when the user requests image-led exploration or when a missing visual decision needs it; ordinary UI edits do not require image generation. Follow the available image tool's actual instructions and the user's asset constraints.

Before coding, inspect the reference and identify its hierarchy, content widths, spacing, type scale, colors, asset roles and interaction intent. Keep the product's real copy and states authoritative. A mockup is visual guidance, not proof that fabricated prices, claims or controls exist.

Generate or inspect only the views needed to resolve uncertainty. Prefer a readable section reference over a tiny full-page board; an extra close-up is useful only if a concrete detail is unclear. Never invent an arbitrary image quota or regenerate every section by default.

Build semantic responsive components in the project's stack. Compare the implemented viewport with the reference, then check a narrower width and important interactions. Preserve keyboard access, contrast, text zoom and reduced-motion behavior. Report remaining visual differences honestly. Read [extraction details](references/extraction.md) when converting a complex image.
