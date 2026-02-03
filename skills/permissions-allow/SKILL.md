---
name: permissions-allow
description: Configure Codex approvals and sandbox defaults in config.toml.
---

# Configure Codex Approvals

This skill configures Codex's approval and sandbox settings. It does not grant OS-level permissions; it only changes Codex config.

## Steps

1. Ask for scope:
   - **Project-level** (recommended for repo-specific behavior)
   - **User-level** (applies everywhere)

2. Ensure the target directory exists:
   - Project-level: `./.codex/`
   - User-level: `~/.codex/`

3. Create or update `config.toml` with these defaults (preserve existing keys if present):

```toml
model = "gpt-5.2"
model_reasoning_effort = "high"
approval_policy = "on-request"
sandbox_mode = "workspace-write"
web_search = "cached"

[features]
web_search_request = true
```

4. If a config already exists, merge by keeping existing values and only filling missing keys.

## Notes

- Use project-level when you want different behavior per repo.
- For stricter command policies or allowlists, use `.codex/rules/` as documented by Codex.
