# Expo / React Native profile

- Detect installed Expo/React Native versions and native folder ownership before changing dependencies or configuration. Follow matching SDK docs and existing Router/navigation, state, styling and testing choices. Do not force Expo Router, NativeWind or a UI kit.
- Use pinned pnpm; use `pnpm expo install` for compatible Expo/native packages. Check compatibility when dependencies change, not as an unconditional startup step. With CNG/prebuild, prefer app config and plugins over edits to generated native folders.
- Keep native UI in React Native primitives with existing styling, safe areas, keyboard behavior, accessibility, offline/error states and lifecycle handling. DOM-only libraries need an intentional supported boundary.
- `EXPO_PUBLIC_*` values are public bundle data. Secrets and privileged operations belong on the backend.
- For authorized delivery, check each platform's runtime, channel and environment. Native dependencies, permissions, plugins, SDK or native config changes need a compatible new binary. Published OTA is distinct from an installed compatible binary and actual device behavior.
- Use the repository's native QA and runtime ownership procedure. Inspect native UI changes on the appropriate simulator/emulator/device; web screenshots or Expo Go alone do not establish production native behavior. Run relevant behavior checks and required repository gates; dependency diagnostics are for compatibility uncertainty.
