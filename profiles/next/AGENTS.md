# Codex Profile: Next.js

Project-level instructions for Next.js and React web applications.

## React / Next.js

- Prefer Server Components and minimize `'use client'`, `useState`, and `useEffect`.
- Wrap client components in `<Suspense>` with a useful fallback when loading them from server-rendered surfaces.
- Use dynamic imports for non-critical client-only components.
- Prefer Server Actions over API Routes when the task fits the App Router model.
- Follow the Next.js docs for Data Fetching, Rendering, Routing, Metadata, and Caching.
- Avoid waterfalls: fetch independent data with `Promise.all()`.
- Use `React.cache()` for functions called multiple times in one render path.
- Import directly instead of using barrels, especially for icon libraries.
- Keep global state in client components; prefer Zustand over React Context for shared client state.

## UI And Styling

- Use Tailwind CSS plus shadcn/ui based on Radix when the project already uses or requests that stack.
- Do not add UI packages unless the repo needs them and the user agrees.
- Add a global `cursor: pointer` rule for interactive elements if the project is missing one.
- Use mobile-first responsive design.
- Match the existing design system before introducing new component patterns.
- Use lucide icons in buttons when an icon exists and the project uses lucide.
- Do not leave shadcn/ui components in their untouched default visual state.

## Performance

- Optimize Web Vitals, especially LCP, CLS, and INP.
- Use explicit image dimensions and modern formats such as WebP or AVIF when appropriate.
- Prefer `next/image` for local/remote images when it fits the project constraints.
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
- Check at least one desktop and one mobile viewport for meaningful UI changes.
- For deterministic assertions, use Playwright or the repo's existing test harness.

## Project Setup Expectations

- Prefer `app/` App Router conventions for new Next.js work unless the project already uses `pages/`.
- Keep `strict: true` in `tsconfig`.
- Prefer the `@/` import alias when configured.
- Respect existing Tailwind version and configuration before editing styling infrastructure.
- If `components.json` exists, follow the local shadcn/ui aliases and component paths.
