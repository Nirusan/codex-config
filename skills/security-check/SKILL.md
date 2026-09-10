---
name: security-check
description: Review security on explicit request or when a change affects a trust boundary, authorization, untrusted execution, or sensitive data handling. Skip routine copy, layout, and unchanged data paths without a security concern.
---

# Review the affected trust boundary

Start read-only. Trace attacker-controlled input through the changed path to privileged operations or sensitive output. Inspect the relevant diff and callers; do not expand into a repository-wide checklist without a reason.

Select checks that match the boundary:
- Authentication and authorization: server-side enforcement, ownership or tenant isolation, role differences, and both allowed and denied cases. Client guards are not enforcement.
- Untrusted input: SQL or command construction, path traversal, SSRF destinations, unsafe rendering, and validation at the point of trust.
- Sessions, OAuth, and webhooks: cookies, session handling, CSRF/CORS policy, redirect constraints, raw-payload signature verification, and replay handling where applicable.
- Files, storage, and secrets: access scope, upload validation, signed URLs, public exposure, credential handling, and logs.
- Abuse and exposure: mass assignment, rate limits, verbose errors, debug exposure, and dependency/configuration changes when relevant to the affected path.
- Database enforcement: relevant RLS policies, grants, ownership checks, and privileged bypasses. Inspect them directly; do not invoke another audit wrapper recursively.
- AI or agent paths: treat retrieved text and tool output as untrusted data; check whether they can cause unauthorized tool actions or disclose secrets.

Use safe local tests or concrete source evidence. Do not run live exploit attempts, load tests, mutate data, or expose credentials as an audit side effect. Carry forward existing authorization for the exact environment and action; a review request alone does not authorize a repair or deployment.

Report findings by impact with file and line, the triggering conditions, evidence, and a specific correction. Separate confirmed issues from unresolved risks. If nothing actionable is found, name the reviewed scope and limits rather than claiming the application is secure.
