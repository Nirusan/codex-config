# Codex Profile: Next.js

Project-level instructions for Next.js and React web applications.

## React / Next.js

- Prefer Server Components and minimize `'use client'`, `useState`, and `useEffect`.
- Wrap client components in `<Suspense>` with a useful fallback when loading them from server-rendered surfaces.
- Use dynamic imports for non-critical client-only components.
- Prefer Server Actions over API Routes when the task fits the App Router model.
- Follow the Next.js docs for Data Fetching, Rendering, Routing, Metadata, and Caching.
- Avoid waterfalls: fetch independent data with `Promise.all()`.
- Use `React.cache()` for render-path memoization when the same server read is called multiple times; do not use it as a substitute for persistent cache invalidation.
- Import directly instead of using barrels, especially for icon libraries.
- Keep global state in client components; prefer Zustand over React Context for shared client state.

## TypeScript And Routing

- Enable `typedRoutes` when the project supports it, and ensure `.next/types/**/*.ts` is included in `tsconfig`.
- Use route-aware helpers such as `PageProps`, `LayoutProps`, and `RouteContext` for App Router files when generated types are available.
- Type App Router `params` and `searchParams` as promises when the installed Next.js version expects it.
- Prefer `next.config.ts` with `NextConfig` in TypeScript projects.

## Server Boundaries And Data Safety

- Use `import 'server-only'` for modules that access secrets, databases, the filesystem, or private environment variables.
- Do not import server-only modules into Client Components.
- Pass serialized DTOs to Client Components instead of raw ORM records, sessions, tokens, or privileged domain objects.
- Centralize environment variable parsing in a server-only module and avoid scattered non-null assertions.

## Mutations, Auth, And Route Handlers

- Treat Server Actions and Route Handlers as public endpoints: validate input, check authorization, and return typed expected-error states.
- Use Server Actions for UI-driven mutations and Route Handlers for webhooks, third-party callbacks, public APIs, and non-UI protocols.
- After mutations, intentionally call `updateTag`, `revalidateTag`, `revalidatePath`, or `redirect` as appropriate.
- Use `useActionState` and `useFormStatus` for progressive form UX when returning validation errors.

## Caching And Rendering

- Choose an explicit cache policy for important server data reads.
- Tag cached data that needs event-driven invalidation.
- Use `updateTag` for read-your-own-writes flows in Server Actions, and `revalidateTag` or `revalidatePath` for broader cache refreshes.
- Avoid legacy or experimental cache APIs unless the project already opts into that caching model.

## UI And Styling

- Use Tailwind CSS plus shadcn/ui based on Radix when the project already uses or requests that stack.
- Do not add UI packages unless the repo needs them and the user agrees.
- Add a global `cursor: pointer` rule for interactive elements if the project is missing one.
- Use mobile-first responsive design.
- Match the existing design system before introducing new component patterns.
- Use lucide icons in buttons when an icon exists and the project uses lucide.
- Do not leave shadcn/ui components in their untouched default visual state.

## Frontend / Design Workflow

- Read local sources of truth before designing:
  - project `AGENTS.md`
  - repo-root `SKILL.md` if present
  - `design-system.md` if present
  - real product copy, labels, states, and data values
  - screenshots, mockups, or references provided by the user
- Prefer the installed skill stack over external generators:
  - `design-director` when the direction is fuzzy or needs a durable brief
  - `taste-skill` as the default premium execution layer for net-new frontend work
  - `redesign-skill` when upgrading an existing interface
  - `minimalist-skill` for calmer product surfaces
  - `soft-skill` for softer or luxury branding
  - `output-skill` when complete, no-placeholder output matters
  - `frontend-skill` as a complementary composition and narrative-structure guide, especially for landing pages
  - `design-principles` for precise app or dashboard surfaces
  - `responsive-frontend-designs` when matching screenshots or references
  - Browser Use / Codex in-app browser for local visual review and iteration
- If a project-level `SKILL.md` from Taste Skill exists, treat it as a repo-specific override on top of this profile.
- Write frontend code directly unless a repo-level workflow explicitly requires another generator.
- Do not treat Taste Skill and `frontend-skill` as equal co-owners of one pass: Taste owns visual direction, while `frontend-skill` checks hierarchy, section flow, and restraint.

## Performance

- Optimize Web Vitals, especially LCP, CLS, and INP.
- Use explicit image dimensions, lazy loading, and modern formats such as WebP or AVIF when appropriate.
- Prefer `next/image` for local/remote images when it fits the project constraints.
- Provide a `sizes` prop for `next/image` when using `fill` or responsive CSS sizing.
- Use `preload` for the single likely LCP image in Next 16+ instead of deprecated `priority`.
- Use `next/font` for app fonts to avoid font-related layout shift.
- Use `next/script` for third-party scripts and choose an intentional loading strategy.
- Avoid layout shifts from dynamic content, late-loading media, and unstable containers.
- Do not use `h-screen` for full-height mobile browser surfaces; prefer dynamic viewport units such as `min-h-[100dvh]`.
- Avoid expensive blur, shadow, or scroll effects on large scrolling containers.

## SEO And Metadata

- Use App Router metadata APIs where applicable.
- Keep page titles, descriptions, Open Graph data, canonical URLs, and robots behavior intentional.
- Preserve real product copy and do not invent claims, metrics, prices, or testimonials.
- Ensure user-facing pages have accessible structure and sensible heading order.

## Local Development And Verification

- Use `pnpm` for all package commands.
- Prefer Portless for local dev URLs when it is configured or requested.
- Use Browser Use or `dev-browser` for local browser inspection, UI flow checks, screenshots, and responsive validation.
- Prefer Browser Use / Codex in-app browser for local app testing and UI inspection on Portless URLs, `localhost`, `127.0.0.1`, `::1`, or `file://`.
- Use Playwright only for deterministic scripted verification, repeated assertions, text/URL extraction, or when Browser Use is unavailable or insufficient.
- If the user explicitly asks for Browser Use or the in-app browser, open/control that surface first; do not substitute terminal-only browser tooling unless it is a secondary verification step.
- Check at least one desktop and one mobile viewport for meaningful UI changes.
- For deterministic assertions, use Playwright or the repo's existing test harness.
- Run `pnpm typecheck` and `pnpm lint` before claiming Next.js or TypeScript changes are ready when those scripts exist.
- Run `pnpm build` after changes to routing, metadata, caching, Server Actions, Next config, or generated route types.

## Local Dev Servers

- When starting a web app dev server, prefer Portless over raw `localhost:<port>` URLs.
- Use the installed `portless` skill when installing, configuring, running, or troubleshooting Portless.
- Prefer `portless` for a package `dev` script, or `portless <app-name> pnpm dev` when an explicit stable name is clearer.
- For parallel Codex agent work, prefer git worktrees plus `portless run pnpm dev` so each worktree gets its own stable URL.
- Report the Portless URL to the user instead of `localhost:3000`.
- Use `portless list` to discover active routes before opening the app in Browser Use or another browser tool.
- Use `PORTLESS=0 pnpm dev` only when Portless is unavailable, incompatible with the task, or the user explicitly asks for a raw localhost port.
- For OAuth provider testing, use the installed `oauth` skill and prefer a supported TLD with `portless proxy start --tld dev`.

## Project Setup Expectations

- Prefer `app/` App Router conventions for new Next.js work unless the project already uses `pages/`.
- Keep `strict: true` in `tsconfig`.
- Prefer `exactOptionalPropertyTypes` and `noUncheckedIndexedAccess` for new strict TypeScript projects when the repo can adopt them without churn.
- Prefer the `@/` import alias when configured.
- Respect existing Tailwind version and configuration before editing styling infrastructure.
- If `components.json` exists, follow the local shadcn/ui aliases and component paths.
