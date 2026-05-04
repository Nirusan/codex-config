# Global Codex Preferences

Global instructions applied across projects. Stack-specific rules belong in project-level Codex profiles such as `next` or `expo`.

---

## Package Manager

- Always use **`pnpm`** instead of `npm` or `yarn`.

## Language

- **Respond in French** unless the user explicitly requests another language.
- Use English for code, commits, docs, technical identifiers, and internal configuration files.
- Internal configuration files should be in English:
  - `AGENTS.md` files
  - Skills instructions
  - Automation prompts

## TypeScript

- Keep TypeScript strict mode enabled (`"strict": true` in `tsconfig`).
- Avoid `any`; use `unknown`, generics, discriminated unions, or proper domain types.
- Prefer inference when obvious and explicit types for public function signatures.

## Code Style

- Prefer functional and declarative code; do not introduce classes unless the framework or library requires them.
- Prefer modularization over duplication.
- Use descriptive names with auxiliary verbs where useful (`isLoading`, `hasError`, `canSubmit`).
- Use the `function` keyword for pure functions.
- Keep syntax concise; avoid unnecessary braces in simple conditionals.
- Prefer absolute imports with the project alias, usually `@/`, when the repo supports it.

## Naming Conventions

- Folders: `kebab-case`.
- Variables and functions: `camelCase`.
- Components: `PascalCase`.
- Component files: `PascalCase` with a type prefix when the project follows that convention (`ButtonAccount.tsx`, `CardAnalytics.tsx`, `ModalSettings.tsx`).
- Other files: `kebab-case`.

## Project Context

- Read local sources of truth first:
  - `AGENTS.md`
  - repo-root `SKILL.md` if present
  - `README.md`, `docs/`, planning docs, and progress trackers
  - `design-system.md` when UI work is involved
  - real product copy, labels, states, and data values
- Follow project-level Codex profile blocks when present:
  - `codex-profile:next`
  - `codex-profile:expo`
- Do not assume a web, Next.js, or Expo stack from the global config alone.

## UI And Design

- Build production-ready interfaces, not generic or cookie-cutter screens.
- Prefer the repo's existing design system, UI primitives, and styling method.
- Do not invent fake product copy, prices, metrics, enum values, or states.
- Preserve an existing `design-system.md` unless the user asks for a redesign.
- Use visual review tools only when they match the runtime: browser tools for web targets, native/simulator/device checks for mobile targets.

## Skill Routing Heuristics

Use the built-in skill system normally. When a task clearly matches a skill, prefer that skill early instead of improvising.

- If resuming after a break or entering an unfamiliar repo state, use `refresh-context`.
- If the user asks what to do next, use `next-task`.
- If the work is implementation-ready, use `implement`.
- If the task would benefit from isolation or parallel branch work, use `worktree-setup`.
- If a bug is flaky, surprising, or resists the obvious fix, use `systematic-debugging` before editing.
- If the request is still fuzzy or product-level, use `brainstorm`, `prd`, `tech-stack`, or `implementation-plan`.
- For frontend or product UI work, prefer the Taste Skill family when visual quality matters.
- Use `frontend-skill` as a secondary composition check for hierarchy, section flow, and restraint.
- Use `setup-next` to add or refresh a Next.js project profile.
- Use `setup-expo` to add or refresh an Expo/React Native project profile.
- Before claiming a fix is done, a feature is ready, or a merge is safe, use `completion-verification`.
- Treat `git-add-commit-push` and `validate-update-push` as explicit endgame skills, not automatic defaults.

## Tools And Documentation

- Prefer local docs first.
- Use MCP servers for library documentation when available, especially Context7 for framework docs.
- Use OpenAI Docs MCP for OpenAI/Codex APIs.
- Use web search only when up-to-date or niche information is needed.
- Prefer Browser Use or `dev-browser` for local browser inspection; prefer simulator/device-oriented validation for native mobile work.
