# Global Codex Preferences

Global instructions applied to all Next.js/React projects.

---

## Package Manager

- Always use **`pnpm`** instead of `npm` or `yarn`

## Language

- **Respond in French** unless I explicitly request another language
- **English** for code, commits, docs, and technical identifiers
- Internal configuration files should be in English:
  - `AGENTS.md` files (global and project-level)
  - Skills instructions
  - Automation prompts

## TypeScript

- **Strict mode** enabled (`"strict": true` in tsconfig)
- Avoid `any` — use `unknown`, generics, or proper typing instead
- Prefer type inference when obvious, explicit types for function signatures

## Code Style

- Functional and declarative, **no classes**
- Modularization > code duplication
- Descriptive names with auxiliary verbs (`isLoading`, `hasError`, `canSubmit`)
- `function` keyword for pure functions
- Concise syntax (avoid unnecessary braces in simple conditionals)
- **Absolute imports** with `@/` alias instead of relative paths (`../../../`)

## Naming Conventions

- **Folders**: `kebab-case`
- **Variables / Functions**: `camelCase`
- **Components**: `PascalCase`
- **Component files**: `PascalCase` with type prefix (`ButtonAccount.tsx`, `CardAnalytics.tsx`, `ModalSettings.tsx`)
- **Other files**: `kebab-case`

## React / Next.js

- Minimize `'use client'`, `useState`, `useEffect`
- Prefer **Server Components** (RSC)
- Wrap client components in `<Suspense>` with fallback
- Dynamic imports for non-critical components
- **State management**: use **Zustand** over React Context for global state
- **Data fetching**: prefer **Server Actions** over API Routes when possible
- Follow Next.js docs for Data Fetching, Rendering, Routing
- **No barrel imports**: import directly (`lucide-react/icons/Check`) not from index
- **No waterfalls**: `Promise.all()` for parallel fetches, never sequential `await`
- **Deduplication**: `React.cache()` for functions called multiple times in a render

## UI & Styling

- **Tailwind CSS** + **shadcn/ui** (based on Radix)
- Mobile-first responsive design
- No additional UI packages unless necessary
- **Cursor pointer** on all interactive elements (buttons, links, selects, etc.) — add global CSS rule in `globals.css` if missing

## Performance

- Optimize Web Vitals (LCP, CLS, FID)
- Images: WebP format, lazy loading, explicit dimensions

## Design

- **Production-ready** designs, not generic or cookie-cutter

## Frontend / Design Workflow

### Default Rule

Do NOT use `gemini-design-mcp` or Gemini-specific frontend tooling unless the user explicitly asks for Gemini or names that MCP.

### Preferred Workflow

For frontend and design work, follow this order:

1. Read the local sources of truth first:
   - `AGENTS.md`
   - repo-root `SKILL.md` if present
   - `design-system.md` if present
   - real product copy, labels, states, and data values
   - screenshots, mockups, or references provided by the user
2. Prefer the installed skill stack over an external generator:
   - `design-director` when the direction is fuzzy or needs a durable brief
   - `frontend-skill` for net-new visually strong UI
   - `design-principles` for precise app or dashboard surfaces
   - `responsive-frontend-designs` when matching screenshots or references
   - `dev-browser` for visual review and iteration
3. Prefer the Taste Skill family for frontend aesthetics when the task matches:
   - `taste-skill` for net-new premium UI
   - `redesign-skill` for upgrading an existing interface
   - `minimalist-skill` for calmer product surfaces
   - `soft-skill` for softer or luxury branding
   - `output-skill` when complete, no-placeholder output matters
4. If a project-level `SKILL.md` from Taste Skill exists, treat it as a repo-specific override on top of the global workflow.
5. Write frontend code directly unless a repo-level workflow explicitly requires another generator.

### Taste Skill Guidance

Taste Skill is part of the preferred global frontend workflow in this config. Use project-level Taste Skill files when a repo needs extra specificity or a stronger local override.

### Guardrails

- Do not invent fake product copy, prices, metrics, or enum values.
- Preserve an existing `design-system.md` unless the user asks for a redesign.
- Use Gemini only as an explicit opt-in tool, never as a mandatory default.

## Tools & Documentation

- Prefer local docs first (`README.md`, `docs/`, `AGENTS.md`, repo-root `SKILL.md`, `design-system.md`)
- Use the `dev-browser` skill for live browser automation or UI inspection instead of a browser MCP server
- `dev-browser` reuses a daemon and named browser instances. If a browser was previously started with `--headless`, stop the daemon with `dev-browser stop` or use a different `--browser` name before expecting a visible window.
- Visible `dev-browser` sessions open in `Google Chrome for Testing`, not necessarily the user's regular Chrome profile. Use `dev-browser --connect` when you want to drive an already-open local Chrome session.
- Prefer `--headless` for repeatable UI checks and automation. Prefer visible mode for debugging layout, focus, hover, animation, or responsive issues.
- Use MCP servers for library documentation when available (Context7)
- Use OpenAI Docs MCP for OpenAI/Codex APIs
- Use web search only when you need up-to-date or niche information
