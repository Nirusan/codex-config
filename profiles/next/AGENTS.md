# Next.js profile

- Detect installed Next/React versions and App Router versus Pages Router. Follow existing routing, styling, aliases and component conventions; use version-matched documentation for caching, metadata and data APIs.
- Keep server-only data and secrets on the server. Add client boundaries for actual interactivity; use Suspense for asynchronous boundaries where a meaningful fallback helps. Authenticate and authorize mutations regardless of whether they use Server Actions or route handlers.
- Fetch independent reads concurrently. Distinguish render memoization from persistent caching; preserve invalidation, user isolation and loading/error behavior.
- Use existing components, real product content and responsive accessible markup. Optimize the actual LCP image and reserve image dimensions; choose supported image/font APIs for the installed version. Avoid expensive effects without an observed need.
- Use pinned pnpm and the configured local server/browser workflow. Use Portless when already configured or requested; respect owned worktree and server resources.
- Inspect meaningful UI changes at relevant desktop/mobile sizes. Run required typecheck/lint and focused behavior tests; build after routing, metadata, caching, server action, Next config or generated route-type changes. Reuse evidence for unchanged revision/environment.
