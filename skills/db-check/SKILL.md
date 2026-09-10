---
name: db-check
description: Review a database schema, migration, RLS policy, grant, function, storage policy, or a requested database health/performance issue. Skip unchanged client queries and tasks with no evidence of a database concern.
---

# Review the database change or issue

1. Establish the exact database object, behavior, and environment in scope. Start with relevant migrations, schema, generated types, and callers. A local review does not require connecting to production.
2. If live evidence is needed, resolve the project and database target from current configuration and task context before using configured Supabase MCP, CLI, or SQL tools. Use scoped read-only inspection; resolve a materially ambiguous target before accessing it.
3. Select the relevant checks:
   - Schema and migrations: constraints, nullability, compatibility with callers, data transformation assumptions, and generated types. Test migrations in a suitable disposable environment or an explicitly authorized target.
   - RLS and grants: enablement, USING and WITH CHECK, ownership or team boundaries, anonymous/authenticated roles, and service-role or administrative bypasses. Exercise allowed and denied cases when possible.
   - Functions: execution grants, privilege level, and a safe search_path for SECURITY DEFINER functions.
   - Storage: bucket exposure and object policies for the relevant read/write operations.
   - Performance: the actual query and workload, filters, pagination, indexes, and relationships. Plain EXPLAIN can inspect a plan; EXPLAIN ANALYZE executes the query and requires an appropriate safe dataset.
4. Treat database advisors as additional evidence, not proof that application authorization or performance is correct.
5. Report the target, findings, supporting evidence, and unverified conditions. Distinguish local migration files, an applied schema, and behavior under real roles.

Do not apply production migrations, alter policies, reset databases, or repair data as a side effect of review. Existing authorization remains valid only for its exact effects and target. Review adjacent authorization in the affected path directly rather than calling security-check recursively.
