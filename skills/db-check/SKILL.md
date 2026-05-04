---
name: db-check
description: Check Supabase/Postgres database health, schema changes, migrations, RLS policies, grants, and advisors when available. Use after creating or modifying database migrations, RLS policies, schema, storage policies, or Supabase data paths. Do not rely on remote advisors alone; report clearly when live database access is unavailable.
---

# Database Check

Use this skill to verify database changes with evidence, not just schema confidence.

## Workflow

1. Identify the database surface:
   - changed migration files
   - schema/types files
   - RLS policies, grants, functions, triggers, storage policies
   - application query or mutation paths touched by the change
2. Check live Supabase access if MCP tools are available:
   - list projects and resolve the intended project/ref
   - list tables and policies
   - run security and performance advisors
3. If Supabase MCP tools are unavailable, do not dead-end.
   - inspect local migrations and schema files
   - use configured Supabase CLI or SQL access only if already available in the repo/environment
   - report live checks as `not verified`
4. For RLS or permission work, inspect policy semantics directly.
   - allowed roles
   - `using` and `with check` expressions
   - ownership/team predicates
   - service role or admin bypass paths
5. For performance-sensitive changes, check indexes, foreign keys, query filters, pagination assumptions, and advisor output when available.
6. If the change also touches app auth, API handlers, or query construction, use `$security-check` for the application layer.

## Rules

- Never say "No issues detected" unless the relevant live or local checks actually ran.
- Distinguish `passed`, `failed`, `not configured`, and `not verified`.
- Include project/ref, files inspected, commands/tools used, and advisor results when available.
- Ask the user to choose only when multiple live projects are available and the target is not inferable.

## Output

Return a concise report:

- scope inspected
- live database access status
- migrations/schema/policies reviewed
- security findings
- performance findings
- checks not verified
- recommended fixes or follow-up
