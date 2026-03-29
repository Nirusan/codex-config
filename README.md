# Codex Configuration

Personal Codex configuration for a consistent development experience across machines.

> ⚠️ **Warning**: This will **overwrite** your existing `~/.codex/` configuration. A backup is automatically created at `~/.codex-backup-YYYYMMDD-HHMMSS/` before installation.

## Prerequisites

- **git** - for cloning and syncing
- **curl** - for one-liner install
- **bash** - shell (macOS/Linux/WSL)

## Quick Install

### User-level (all projects on this machine)

```bash
# One-liner
curl -sSL https://raw.githubusercontent.com/Nirusan/codex-config/main/install.sh | bash

# Or from clone
git clone https://github.com/Nirusan/codex-config.git
cd codex-config
./install.sh --user
```

### Project-level (current project only)

```bash
# One-liner
curl -sSL https://raw.githubusercontent.com/Nirusan/codex-config/main/install.sh | bash -s -- --project

# Or from clone
git clone https://github.com/Nirusan/codex-config.git /tmp/codex-config
cd /path/to/your/project
/tmp/codex-config/install.sh --project
```

## Installation Modes

| Mode | Flag | Target | Use Case |
|------|------|--------|---------|
| **User** | `--user` (default) | `~/.codex/` | Personal machine, all projects |
| **Project** | `--project` | `./.codex/` + `./AGENTS.md` | Team config, repo-specific rules |

### Options

| Flag | Description |
|------|-------------|
| `--yes` or `-y` | Skip confirmation prompt (for CI/Docker) |

### Existing config protection

If you already have a Codex config, the installer will:
1. **Warn you** (EN/FR) that your config will be overwritten
2. **Ask for confirmation** (press `y` to continue, any other key to abort)
3. **Create a backup** at `~/.codex-backup-YYYYMMDD-HHMMSS/`

To restore your previous config:
```bash
cp -rP ~/.codex-backup-YYYYMMDD-HHMMSS/* ~/.codex/
```

---

## What's Included

### Global Instructions

- `config/AGENTS.md` → installed to `~/.codex/AGENTS.md` (or `./AGENTS.md` for project mode)
- Global development conventions (TypeScript, Next.js, naming, style)
- French responses, English code/docs

### Codex Config

- `config/config.example.toml` → installed to `~/.codex/config.toml` (or `./.codex/config.toml`)
- Public-safe template only: no real API keys or personal project paths are stored in this repo
- Model defaults, approvals, sandbox mode, web search
- MCP server templates (OpenAI Docs, Context7, Brave, Firecrawl, Supabase, Exa, Chrome DevTools, Gemini Design, n8n)

### Skills

All skills live in `skills/` and are installed to `~/.codex/skills/` or `./.codex/skills/`.

BMAD Lite workflow:
- `brainstorm` → product brief in `memory-bank/brief.md`
- `prd` → requirements in `memory-bank/prd.md`
- `tech-stack` → architecture in `memory-bank/tech-stack.md`
- `implementation-plan` → stories in `memory-bank/plan.md`
- `implement` → read context, code one story, validate, update progress

Development & validation:
- `validate`, `validate-quick`, `validate-update-push`
- `next-task`, `refresh-context`, `update-progress`
- `git-add-commit-push`

Quality & utilities:
- `security-check`, `db-check`, `seo-check`, `design-principles`
- `humanizer`, `update-docs`, `sync-config`, `permissions-allow`

---

## Updating

```bash
cd /path/to/codex-config
git pull
./install.sh
```

## Sync local changes back to repo

```bash
cd /path/to/codex-config
./sync.sh
```

`./sync.sh` updates `config/config.example.toml`, not your real local `config.toml`. Review the generated template before committing to make sure it only contains placeholders.

## File Structure

```
codex-config/
├── README.md
├── README.fr.md
├── install.sh
├── sync.sh
├── config/
│   ├── AGENTS.md
│   └── config.example.toml
└── skills/
    ├── brainstorm/SKILL.md
    ├── prd/SKILL.md
    ├── tech-stack/SKILL.md
    ├── implementation-plan/SKILL.md
    ├── implement/SKILL.md
    ├── validate/SKILL.md
    ├── validate-quick/SKILL.md
    ├── validate-update-push/SKILL.md
    ├── next-task/SKILL.md
    ├── refresh-context/SKILL.md
    ├── update-progress/SKILL.md
    ├── git-add-commit-push/SKILL.md
    ├── security-check/SKILL.md
    ├── db-check/SKILL.md
    ├── seo-check/SKILL.md
    ├── design-principles/SKILL.md
    ├── update-docs/SKILL.md
    ├── humanizer/SKILL.md
    ├── permissions-allow/SKILL.md
    └── sync-config/SKILL.md
```

---

## License

MIT - Feel free to fork and customize.
