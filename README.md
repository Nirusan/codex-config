# Codex Configuration

Personal Codex configuration for a consistent development experience across machines and stacks.

> Warning: user-level installation updates `~/.codex/`. A backup is created at `~/.codex-backup-YYYYMMDD-HHMMSS/` before installation. Project profile installs preserve human-written `AGENTS.md` content outside marked profile blocks.

## Prerequisites

- **git** - cloning and syncing
- **curl** - one-liner install
- **bash** - shell (macOS/Linux/WSL)
- **python3** - idempotent project profile updates

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

### Project-level profiles

```bash
# Neutral project config
curl -sSL https://raw.githubusercontent.com/Nirusan/codex-config/main/install.sh | bash -s -- --project

# Next.js project profile
curl -sSL https://raw.githubusercontent.com/Nirusan/codex-config/main/install.sh | bash -s -- --project --profile next

# Expo / React Native project profile
curl -sSL https://raw.githubusercontent.com/Nirusan/codex-config/main/install.sh | bash -s -- --project --profile expo
```

From a local clone:

```bash
git clone https://github.com/Nirusan/codex-config.git /tmp/codex-config
cd /path/to/your/project
/tmp/codex-config/install.sh --project --profile next
```

The one-liner mode fetches a complete temporary copy of this repo before installing, so nested skill resources such as `agents/`, `scripts/`, `references/`, and `assets/` are preserved just like a local clone install.

For monorepos, target a specific app folder:

```bash
/tmp/codex-config/install.sh --project --profile next --target apps/web
/tmp/codex-config/install.sh --project --profile expo --target apps/mobile
```

## Installation Modes

| Mode | Flag | Target | Use Case |
|------|------|--------|----------|
| User | `--user` (default) | `~/.codex/` | Personal machine, all projects |
| Project | `--project` | `./.codex/` + `./AGENTS.md` | Team or repo-specific neutral config |
| Project profile | `--project --profile next\|expo` | target `.codex/` + profile block in `AGENTS.md` | Stack-specific project quality |

Options:

| Flag | Description |
|------|-------------|
| `--yes` or `-y` | Skip confirmation prompt |
| `--profile next` | Apply or refresh the Next.js Codex profile |
| `--profile expo` | Apply or refresh the Expo / React Native Codex profile |
| `--target path` | Apply project config to a specific folder |

Remote-source overrides:

| Env var | Description |
|---------|-------------|
| `SOURCE_REPO_URL` | Git repository used by remote one-liner installs |
| `SOURCE_BRANCH` | Branch to clone or download, default `main` |
| `ARCHIVE_URL` | Tarball fallback when Git clone is unavailable |

## Project Profiles

This repo uses a layered setup:

- `config/AGENTS.md` is the neutral global baseline.
- `profiles/next/AGENTS.md` contains Next.js / React web rules.
- `profiles/expo/AGENTS.md` contains Expo / React Native rules.
- `scripts/apply-profile.py` inserts or refreshes a profile block in project `AGENTS.md`.

Profile installs are idempotent and preserve all content outside these markers:

```md
<!-- codex-profile:next:start -->
...
<!-- codex-profile:next:end -->
```

```md
<!-- codex-profile:expo:start -->
...
<!-- codex-profile:expo:end -->
```

Use `$setup-next` or `$setup-expo` inside Codex to apply the matching profile and get a short audit of the project configuration.

## What's Included

### Global Instructions

- Neutral TypeScript, naming, style, validation, docs, and skill-routing conventions
- French responses, English code/docs/internal config
- Stack-specific rules kept out of the global baseline

### Codex Config

- `config/config.example.toml` -> `~/.codex/config.toml` or `./.codex/config.toml`
- Public-safe template only: no real API keys or personal paths
- MCP server templates for OpenAI Docs, Context7, Brave, Firecrawl, Supabase, Exa, n8n
- Browser automation via the `dev-browser` skill/CLI instead of a browser MCP server

### Skills

Core workflow:
- `refresh-context` -> recover project state before resuming work
- `brainstorm`, `prd`, `tech-stack`, `implementation-plan` -> shape ideas into buildable plans
- `next-task`, `implement`, `update-progress` -> choose, execute, and record work
- `setup-next`, `setup-expo` -> apply and audit stack-specific project profiles

Debugging, validation, and release hygiene:
- `systematic-debugging` -> root-cause-first debugging
- `validate`, `validate-quick`, `completion-verification` -> readiness checks
- `validate-update-push`, `git-add-commit-push` -> explicit endgame workflows
- `security-check`, `db-check`, `seo-check`

Design and UI:
- `design-director`, `design-principles`, `frontend-skill`
- `taste-skill`, `redesign-skill`, `minimalist-skill`, `soft-skill`, `output-skill`
- `responsive-frontend-designs`, `dev-browser`, `browser-based-games`

Recommended frontend workflow:
- Keep Gemini Design out of the default config unless explicitly requested.
- Apply `$setup-next` for serious Next.js projects and `$setup-expo` for serious Expo / React Native projects.
- Use Taste Skill as the primary aesthetic execution layer and `frontend-skill` as a secondary composition check.
- Let repo-local `SKILL.md` files add project-specific overrides.

## Browser Automation Setup

This repo uses `dev-browser` for live browser automation.

```bash
pnpm add -g dev-browser
dev-browser install
dev-browser --help
```

## Updating

```bash
cd /path/to/codex-config
git pull
./install.sh
```

## Sync Local Changes Back To Repo

```bash
cd /path/to/codex-config
./sync.sh
```

`./sync.sh` updates `config/config.example.toml`, syncs full skill directories, and also syncs `profiles/` plus `scripts/apply-profile.py` when present in `~/.codex/`. Review generated config before committing.

## File Structure

```text
codex-config/
├── README.md
├── README.fr.md
├── install.sh
├── sync.sh
├── config/
│   ├── AGENTS.md
│   └── config.example.toml
├── profiles/
│   ├── next/
│   │   └── AGENTS.md
│   └── expo/
│       └── AGENTS.md
├── scripts/
│   └── apply-profile.py
└── skills/
    ├── setup-next/
    │   ├── SKILL.md
    │   └── agents/openai.yaml
    ├── setup-expo/
    │   ├── SKILL.md
    │   └── agents/openai.yaml
    └── ...
```

## License

MIT - Feel free to fork and customize.
