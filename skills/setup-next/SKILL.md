---
name: setup-next
description: Use when configuring or refreshing Codex instructions for a Next.js project. Applies or updates the Next Codex profile in AGENTS.md, inspects project configuration, and reports a compact audit without changing application code.
---

# Setup Next

Use this skill to prepare a Next.js repo, app folder, or monorepo package for high-quality Codex work.

## Workflow

1. Resolve the target directory:
   - default to the current working directory
   - use the user-provided path when they name one
2. Apply the Next profile with the shared helper when available:
   ```bash
   python3 "${CODEX_HOME:-$HOME/.codex}/scripts/apply-profile.py" --profile next --target "$TARGET_DIR"
   ```
   If the helper is not installed but this config repo is present, use `scripts/apply-profile.py` from the repo. If no helper exists, update `AGENTS.md` manually using `codex-profile:next` markers.
3. Inspect, but do not modify, the project:
   - `package.json`
   - `next.config.*`
   - `tsconfig.json`
   - `app/` or `pages/`
   - `tailwind.config.*`, `postcss.config.*`, `components.json`
   - package scripts for lint, typecheck, test, build, and dev
4. Report a short audit:
   - profile applied or refreshed
   - detected Next routing model
   - TypeScript and import alias status
   - styling/UI stack detected
   - missing or suspicious validation scripts
   - recommended validation commands

## Rules

- Only update the `codex-profile:next` block in `AGENTS.md`.
- Preserve all human-written content outside the profile block.
- Do not install dependencies.
- Do not edit app code, config files, `tsconfig`, or package scripts in v1.
- Prefer project facts over assumptions when reporting the audit.
- If the target is not a Next.js project, say so and still apply the profile only if the user explicitly asked for setup.
