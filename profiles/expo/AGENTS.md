# Codex Profile: Expo / React Native

Project-level instructions for Expo and React Native applications.

## Expo And React Native

- Treat Expo as the native runtime source of truth; do not apply web-only Next.js patterns.
- Use `pnpm` for package scripts.
- For Expo-compatible native packages, prefer `pnpm expo install <package>` so versions match the installed Expo SDK.
- Respect the existing app architecture instead of forcing Expo Router, NativeWind, EAS, or a UI kit.
- If Expo Router is already present, follow file-based routing conventions and use typed routes when configured.
- If the project uses React Navigation directly, preserve that navigation model.
- Prefer `app.config.ts` or `app.json` plus config plugins for native configuration.
- With Continuous Native Generation or prebuild, avoid hand-editing `ios/` and `android/` unless the repo clearly owns native folders.

## Expo Skills

- Use the official Expo companion skills when the task matches their scope, while keeping this profile and project-local conventions authoritative.
- Adapt package-manager examples from imported Expo skills to this config's `pnpm` preference unless a project script or Expo/EAS CLI requirement says otherwise.
- Use `building-native-ui` for Expo Router UI, native navigation patterns, animations, media, visual effects, storage, tabs, search, and native controls.
- Use `native-data-fetching` for network requests, API calls, caching, offline behavior, retry/error states, auth tokens, and Expo Router loaders.
- Use `expo-api-routes` for Expo Router server routes, EAS Hosting API endpoints, server-side secrets, webhooks, and backend validation.
- Use `expo-dev-client` for custom development builds, native modules, dev-client distribution, and Expo Go vs dev-build decisions.
- Use `expo-module` when building or modifying Expo native modules, native views, config plugins, lifecycle hooks, or autolinking.
- Use `expo-tailwind-setup` only when adding or maintaining Tailwind CSS v4, NativeWind v5, or `react-native-css`.
- Use `expo-ui-swift-ui` for `@expo/ui/swift-ui` work and `expo-ui-jetpack-compose` for `@expo/ui/jetpack-compose` work.
- Use `use-dom` when running web-only React components inside Expo DOM components or migrating web code incrementally to native.
- Use `upgrading-expo` for Expo SDK upgrades, New Architecture migration, React 19/Compiler changes, native tabs changes, and deprecated package replacements.
- Use `expo-cicd-workflows` for `.eas/workflows/` YAML, EAS CI/CD pipelines, and workflow schema validation.
- Use `expo-deployment` for EAS Build, App Store, Play Store, TestFlight, web hosting, and production submission flows.
- Use `eas-update-insights` for published EAS Update health, crash rates, launch/install counts, payload size, and OTA-vs-embedded rollout checks.

## TypeScript And Structure

- Keep `strict: true` and extend Expo's base TypeScript config when the project does so.
- Prefer the `@/` import alias when configured in `tsconfig` and Babel/Metro.
- Keep components functional and typed.
- Keep screen, component, hook, and utility boundaries small enough for mobile flows to stay readable.
- Use platform-specific files such as `.ios.tsx`, `.android.tsx`, or `.native.tsx` only when behavior truly differs.

## Native UI And Styling

- Use React Native primitives (`View`, `Text`, `Pressable`, `TextInput`, `Image`, lists) and the project's existing styling system.
- If NativeWind is already installed, follow its local conventions; do not add it by default.
- If the project uses `StyleSheet`, keep styles colocated and typed where practical.
- Account for safe areas, keyboard avoidance, status bar treatment, and platform differences.
- Prefer `Pressable` for custom touch interactions.
- Keep touch targets accessible and large enough for mobile use.
- Do not import DOM-only, Radix, shadcn/ui, or web browser APIs into native code.

## State, Data, And Effects

- Keep local state local; use Zustand for global client state when the project needs shared state.
- Minimize `useEffect`; prefer declarative data flows and existing data-fetching utilities.
- Avoid sequential awaits for independent data.
- Handle loading, empty, error, offline, and retry states in mobile-facing flows.
- Be careful with app lifecycle, background/foreground transitions, permissions, and deep links.

## Performance

- Use `FlatList`, `SectionList`, or optimized list primitives for long lists.
- Provide stable keys and avoid inline render work that causes unnecessary list re-renders.
- Use memoization only where it protects real render cost.
- Avoid large images without explicit dimensions or resizing strategy.
- Keep animations off the React render loop when possible.
- Watch bundle size and native startup impact when adding dependencies.

## Accessibility

- Add meaningful `accessibilityLabel`, `accessibilityHint`, `accessibilityRole`, and state props where needed.
- Support dynamic text sizes unless the design explicitly prevents it.
- Verify important flows with screen reader expectations in mind.
- Ensure color contrast and disabled states are clear on small screens.

## Local Development And Verification

- Prefer development builds for apps that depend on custom native modules or native configuration.
- Use Expo Go only when the project fits Expo Go constraints.
- Use `pnpm expo start`, platform-specific simulator commands, and the repo's existing scripts for local validation.
- Run `pnpm expo-doctor` or `npx expo-doctor@latest` when dependency compatibility is uncertain.
- Validate UI changes on a simulator, emulator, or device when the change affects native behavior.
- For tests, prefer the repo's existing Jest, React Native Testing Library, Maestro, Detox, or Expo test setup.
