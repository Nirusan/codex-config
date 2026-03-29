---
name: sync-config
description: Sync local Codex config (AGENTS.md, a public-safe config template, and full skill directories) to this repo.
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

- This syncs:
  - `AGENTS.md`
  - `config/config.example.toml` generated from your local `config.toml` with placeholders instead of real secrets
  - full `skills/<name>/` directories, including nested `agents/`, `scripts/`, `references/`, and `assets/`
- The real local `config.toml` must never be committed to this public repo
- Review the generated `config/config.example.toml` before pushing to confirm it contains placeholders only
