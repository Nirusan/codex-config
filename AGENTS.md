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

## MCP Gemini Design - Mandatory Unique Workflow

### Absolute Rule

You NEVER write frontend/UI code yourself. Gemini is your frontend developer.

### Available Tools

- `generate_vibes`: Generates a visual page with 5 differently styled sections. The user opens the page, sees all 5 vibes, and picks their favorite. The code from the chosen vibe becomes `design-system.md`.
- `create_frontend`: Creates a NEW complete file (page, component, section).
- `modify_frontend`: Makes ONE design modification to existing code. Returns a FIND/REPLACE block to apply.
- `snippet_frontend`: Generates a code snippet to INSERT into an existing file. For adding elements without rewriting the entire file.

### Workflow (No Alternatives)

#### Step 1: Check for `design-system.md`

BEFORE any frontend call, check if `design-system.md` exists at project root.

#### Step 2A: If `design-system.md` DOES NOT EXIST

1. Call `generate_vibes` with `projectDescription`, `projectType`, `techStack`.
2. Receive the code for a page with 5 visual sections.
3. Ask: "You don't have a design system. Can I create vibes-selection.tsx so you can visually choose your style?"
4. If yes, write the page to the file.
5. User chooses: "vibe 3" or "the 5th one".
6. Extract THE ENTIRE CODE between `<!-- VIBE_X_START -->` and `<!-- VIBE_X_END -->`.
7. Save it to `design-system.md`.
8. Ask: "Delete vibes-selection.tsx?"
9. Continue normally.

#### Step 2B: If `design-system.md` EXISTS

Read it and use its content for frontend calls.

#### Step 3: Frontend Calls

For EVERY call (`create_frontend`, `modify_frontend`, `snippet_frontend`), you MUST pass:

- `designSystem`: Copy-paste the ENTIRE content of `design-system.md` (all the code, not a summary).
- `context`: Functional/business context WITH ALL REAL DATA. Include:
  - What it does, features, requirements.
  - ALL real text/labels to display (status labels, button text, titles...).
  - ALL real data values (prices, stats, numbers...).
  - Enum values and their exact meaning.
  - Any business-specific information.

WHY: Gemini will use placeholders `[Title]`, `[Price]` for missing info. If you don't provide real data, you'll get placeholders or worse - fake data.

### Forbidden

- Writing frontend without Gemini.
- Skipping the vibes workflow when `design-system.md` is missing.
- Extracting "rules" instead of THE ENTIRE code.
- Manually creating `design-system.md`.
- Passing design/styling info in `context` (that goes in `designSystem`).
- Summarizing the design system instead of copy-pasting it entirely.
- Calling Gemini without providing real data (labels, stats, prices, etc.) → leads to fake info.

### Expected

- Check for `design-system.md` BEFORE anything.
- Follow the complete vibes workflow if missing.
- Pass the FULL `design-system.md` content in `designSystem`.
- Pass functional context in `context` (purpose, features, requirements).

### Exceptions (You Can Code These Yourself)

- Text-only changes.
- JS logic without UI.
- Non-visual bug fixes.
- Data wiring (`useQuery`, etc.).

## Tools & Documentation

- Prefer local docs first (`README.md`, `docs/`, `AGENTS.md`)
- Use the `dev-browser` skill for live browser automation or UI inspection instead of a browser MCP server
- Use MCP servers for library documentation when available (Context7)
- Use OpenAI Docs MCP for OpenAI/Codex APIs
- Use web search only when you need up-to-date or niche information
