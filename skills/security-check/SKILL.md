---
name: security-check
description: Red-team security audit for code changes. Use automatically when working on authentication, authorization, user inputs, API endpoints, server actions, database queries, payments, webhooks, file uploads, storage, secrets, AI/tool execution, or other security-sensitive code. Also use before commits that touch sensitive areas.
---

# Security Check

Use this skill to audit the changed behavior like an attacker would, with evidence and clear uncertainty.

## Workflow

1. Define the scope from actual changes:
   - `git diff` or staged diff
   - touched files and routes/actions
   - data flow from user input to persistence, external services, or privileged operations
2. Identify trust boundaries:
   - browser to server
   - server actions or API routes
   - database and RLS
   - webhooks and third-party callbacks
   - file/object storage
   - AI tools, generated code, or command execution
3. Review the relevant attack surfaces:
   - injection: SQL/NoSQL, command, template, path traversal, SSRF
   - XSS and unsafe HTML/Markdown rendering
   - authentication, authorization, IDOR, privilege escalation
   - CSRF, CORS, cookies, sessions, JWT handling
   - OAuth redirects/callbacks and webhook signature verification
   - file uploads, MIME/type checks, storage permissions, signed URLs
   - secrets in code, logs, client bundles, URLs, or environment handling
   - rate limits, abuse paths, mass assignment, verbose errors
   - dependency/config risks and production debug exposure
   - prompt injection, tool injection, and untrusted AI-generated actions
4. For database schema, migrations, RLS, grants, or storage policies, use `$db-check` for the database layer.
5. Verify realistic exploitability.
   - compare allowed and denied paths
   - inspect both client and server enforcement
   - prefer concrete code evidence over checklist completion
6. Report only what was inspected.

## Rules

- Include file paths and line numbers for findings.
- Separate confirmed issues from risks, assumptions, and unverified areas.
- Do not list a passed check unless you actually inspected the relevant code path.
- Consider full attack chains, not only isolated vulnerabilities.
- Provide actionable fixes with the smallest safe scope.

## Output

Return a concise report:

- scope inspected
- evidence used: files, commands, logs, or flows
- risk level: Critical, High, Medium, Low, or No confirmed issues
- confirmed findings ordered by severity
- unverified areas and why
- recommended fixes or follow-up checks
