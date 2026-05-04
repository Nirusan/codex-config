---
name: validate
description: "Run full project validation using the repo's real scripts: lint, typecheck, build, and all relevant tests. Use when the user asks for full validation, a full test pass, or deeper merge/release confidence. Do not use for a quick pre-commit signal; use validate-quick for that, and use completion-verification before making readiness claims."
---

# Full Project Validation

Use this skill when a broad validation pass is needed, not just a quick health check.

## Workflow

1. Read the repo's validation guidance first:
   - `AGENTS.md`
   - `README.md`
   - CI config if present
   - `package.json` scripts
2. Detect available scripts and prefer the repo's documented validation command when one exists.
3. If no single documented command exists, run the applicable checks in this order:
   - `pnpm lint`
   - `pnpm typecheck`
   - `pnpm build`
   - unit or integration tests such as `pnpm test`, `pnpm test:unit`, or `pnpm test:integration`
   - E2E tests such as `pnpm test:e2e`
4. Run every distinct relevant test layer that exists.
   - Do not treat unit tests as a fallback for E2E tests.
   - If one script clearly wraps another, avoid duplicate runs and say why.
5. Stop immediately on the first failure unless the user explicitly asks for a full failure inventory.
6. Read the output and report only what actually ran.

## Rules

- Use `pnpm`, not `npm` or `yarn`.
- Skip missing scripts with a note; do not invent validation commands.
- Prefer the repo's CI-equivalent command when it is clearly documented.
- Do not claim the feature is ready based only on generic project validation; use `$completion-verification` for readiness claims.

## Output

Return a compact summary:

- commands run
- commands skipped and why
- first failure, if any
- what the result does and does not prove
