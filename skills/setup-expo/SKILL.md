---
name: setup-expo
description: Use when configuring or refreshing Codex instructions for an Expo or React Native project. Applies or updates the Expo Codex profile in AGENTS.md, inspects project configuration, and reports a compact audit without changing application code.
---

# Setup Expo

Use this skill to prepare an Expo or React Native repo, app folder, or monorepo package for high-quality Codex work.

## Workflow

1. Resolve the target directory:
   - default to the current working directory
   - use the user-provided path when they name one
2. Apply the Expo profile with the shared helper when available:
   ```bash
   python3 "${CODEX_HOME:-$HOME/.codex}/scripts/apply-profile.py" --profile expo --target "$TARGET_DIR"
   ```
   If the helper is not installed but this config repo is present, use `scripts/apply-profile.py` from the repo. If no helper exists, update `AGENTS.md` manually using `codex-profile:expo` markers.
3. Inspect, but do not modify, the project:
   - `package.json`
   - `app.json`, `app.config.*`, `eas.json`
   - `tsconfig.json`, `babel.config.*`, `metro.config.*`
   - `app/`, `src/`, `ios/`, `android/`
   - Expo Router, React Navigation, NativeWind, Zustand, test tooling
   - package scripts for lint, typecheck, test, doctor, dev, ios, android, and build
4. Report a short audit:
   - profile applied or refreshed
   - Expo SDK and React Native signals detected
   - routing model detected
   - TypeScript and import alias status
   - native configuration and EAS/dev build signals
   - missing or suspicious validation scripts
   - recommended validation commands

## Rules

- Only update the `codex-profile:expo` block in `AGENTS.md`.
- Preserve all human-written content outside the profile block.
- Do not install dependencies.
- Do not edit app code, native folders, config files, `tsconfig`, or package scripts in v1.
- Keep the profile adaptive: do not force Expo Router, NativeWind, EAS, or a UI library.
- Prefer project facts over assumptions when reporting the audit.
- If the target is not an Expo or React Native project, say so and still apply the profile only if the user explicitly asked for setup.
