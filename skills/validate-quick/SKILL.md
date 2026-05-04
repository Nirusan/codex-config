---
name: validate-quick
description: Quick validation check returning a compact pass/fail signal before commit, push, or a lightweight readiness claim. Runs the fastest meaningful checks available for the repo, preferring lint or type checks over heavier validation, and only falls back to broader checks when the repo lacks a lighter trustworthy gate.
---

# Quick Validation Check

Use this skill when you need a fast confidence signal, not a full QA pass.

## Use when

- before commit or push
- when the user asks "is it ready?" and a quick signal is enough
- when you want a lightweight preflight before deeper validation

## Don't use when

- the user wants full validation output
- the claim depends on a specific repro path rather than generic project health
- you already know the change needs deeper testing

## Process

1. Inspect `package.json` or the repo tooling to find the fastest meaningful checks.
2. Prefer this order:
   - `pnpm lint`
   - `pnpm typecheck`
   - `pnpm build` only when no lighter structural check exists or build is the repo's real fast gate
3. Run at most the minimum needed to produce a credible quick signal.
4. Return compact pass/fail output with the exact commands run and skipped.

## Output format

**All pass**
```md
✅ Quick validation passed
- Lint: OK
- Typecheck: OK
```

**Failure**
```md
❌ Quick validation failed
- Lint: FAILED
- Typecheck: Skipped
```

## Rules

- No long error dump; use `$validate` for detailed output.
- Do not pretend this replaces task-specific verification.
- Do not imply skipped checks passed.
- If the repo's only meaningful gate is heavier, say so plainly.
