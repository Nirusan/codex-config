---
name: sync-config
description: Sync local Codex config (AGENTS.md, config.toml, skills) to this repo.
---

# Sync Codex Configuration

Sync your local `~/.codex/` config to the GitHub repo.

## Steps

1. Run the sync script:
```bash
cd ~/Sites/codex-config && ./sync.sh
```

2. Review changes:
```bash
cd ~/Sites/codex-config && git status && git diff
```

3. If changes look good, commit and push:
```bash
cd ~/Sites/codex-config && git add -A && git commit -m "sync: update config" && git push
```

## Notes

- This syncs: `AGENTS.md`, `config.toml`, and `skills/*/SKILL.md`
- Review for secrets before pushing (MCP API keys, tokens)
