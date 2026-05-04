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
   - relevant Expo companion skills to use next, when the project facts point to them

## Companion Expo Skills

This config installs the official Expo skills from `expo/skills`. Prefer these task-specific skills after setup when their scope matches the work:

- `building-native-ui` for Expo Router UI, navigation, animations, media, storage, tabs, search, and native controls.
- `native-data-fetching` for network requests, API calls, caching, offline behavior, retries, auth tokens, and Expo Router loaders.
- `expo-api-routes` for Expo Router API routes, EAS Hosting API endpoints, webhooks, server-side secrets, and backend validation.
- `expo-dev-client` for custom development builds, native modules, and Expo Go vs dev-build decisions.
- `expo-module` for native modules, native views, config plugins, lifecycle hooks, and autolinking.
- `expo-tailwind-setup` for Tailwind CSS v4, NativeWind v5, and `react-native-css`.
- `expo-ui-swift-ui` and `expo-ui-jetpack-compose` for `@expo/ui` native UI work.
- `use-dom` for Expo DOM components and incremental web-to-native migrations.
- `upgrading-expo` for SDK upgrades, New Architecture, React 19/Compiler, native tabs, and deprecated package replacements.
- `expo-cicd-workflows` for `.eas/workflows/` YAML and EAS CI/CD schema validation.
- `expo-deployment` for EAS Build, App Store, Play Store, TestFlight, web hosting, and submissions.
- `eas-update-insights` for published EAS Update health, crash rates, launch/install counts, payload size, and rollout checks.

## Rules

- Only update the `codex-profile:expo` block in `AGENTS.md`.
- Preserve all human-written content outside the profile block.
- Do not install dependencies.
- Do not edit app code, native folders, config files, `tsconfig`, or package scripts in v1.
- Keep the profile adaptive: do not force Expo Router, NativeWind, EAS, or a UI library.
- Prefer project facts over assumptions when reporting the audit.
- If the target is not an Expo or React Native project, say so and still apply the profile only if the user explicitly asked for setup.
