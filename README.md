# Codex Configuration

Personal Codex configuration for a consistent development experience across machines and stacks.

> Warning: user-level installation updates `~/.codex/`. An instruction/resource backup is created at a unique `~/.codex-backup-YYYYMMDD-HHMMSS-XXXXXX/` path before installation; sessions and logs are excluded. Existing `config.toml` settings are preserved. Project profile installs preserve human-written `AGENTS.md` content outside marked profile blocks.

## Prerequisites

- **git** - cloning and syncing
- **curl** - one-liner install
- **bash** - shell (macOS/Linux/WSL)
- **python3 (3.9+)** - resource validation/copying and idempotent project profile updates

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

The one-liner mode fetches a complete temporary copy of this repo before installing. The shared `scripts/copy-resources.py` helper preserves nested skill resources such as `agents/`, `scripts/`, `references/`, and `assets/`, including executable permissions. Both installation paths use the same preflight and resource filters.

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

- Compact cross-project preferences and evidence/authorization boundaries; task-specific instructions stay in project references
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

Expo companion skills:
- Official Expo skills from [expo/skills](https://github.com/expo/skills), vendored under `skills/` and installed with this config.
- UI, native, and runtime: `building-native-ui`, `expo-dev-client`, `expo-module`, `expo-ui-swift-ui`, `expo-ui-jetpack-compose`, `use-dom`
- Data, server, and styling: `native-data-fetching`, `expo-api-routes`, `expo-tailwind-setup`
- Release and operations: `upgrading-expo`, `expo-cicd-workflows`, `expo-deployment`, `eas-update-insights`

Skill selection:
- Keep the existing project design authoritative. Choose a style skill when that direction is requested; do not stack several design procedures for a routine UI change.
- Generic workflow helpers and optional styles/tools remain available by explicit `$skill-name` invocation. Their `agents/openai.yaml` sets `allow_implicit_invocation: false` so they do not consume routine skill catalogue context.
- Specialized automatic skills use narrow task triggers. The manifest `config/skills-manifest.txt` lists all installable directories, including nested resources; it is independent of invocation policy.
- The installer preserves unknown local skills. Remove or retire a directory only after auditing its callers and retaining a recoverable copy.
- Project profiles are compact; `apply-profile.py --check` previews changes. A `codex-profile:<name>:integrated` marker preserves equivalent project-maintained guidance instead of appending a duplicate.

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

`./sync.sh` requires this destination repository's `config/skills-manifest.txt` and copies only its listed skill directories, plus instructions, profiles, and both Python helpers. This public allowlist is never replaced by a personal source manifest. Use `--source <directory>` for another configuration source. Personal skill overlays and other unlisted source/destination files remain in place; adding a skill to the public allowlist requires an intentional review. The script never stages, commits or pushes.

Both scripts validate all selected sources and managed destinations before changing target files. Internal source links are materialized as regular content within the same skill/profile directory; links to sibling skills, external paths, excluded files, dangling targets, and cycles are refused. Global source `AGENTS.md` must itself be a regular file. Existing links in managed destinations are always refused, including internal links left by older installs. For that migration, first back up the exact links and verify their intended in-directory targets, then explicitly replace those links with regular copies before retrying; the scripts never perform this migration automatically.

Transport excludes `.git` files/directories, dependency/cache directories, incidental metadata, `.env`/`.env.*`, `auth.json`, and `config.toml`. Skill-relative runtime paths are also excluded: `company.json`, `copros.json`, `copros/`, `output/`, `data/journal-entries.json`, `data/transactions/`, `data/imports/`, and `data/invoices/` except `_template.json`. Existing destination data at these paths is preserved. Reference data, `company.example.json`, templates, and evaluation examples remain transportable. These are explicit path filters, not a general secret scanner: review newly allowlisted resources before publication.

Local `config.toml` is never exported. Maintain `config/config.example.toml` separately with placeholders. New installs receive the template; instruction refreshes preserve existing model, tool, credential and approval settings.

For Claude Code, keep the same project rules as the canonical content and use a small `CLAUDE.md` import (`@AGENTS.md`) after reconciling any existing Claude rules. Codex invocation policy is product-specific: an intentional Claude copy of an explicit-only skill needs `disable-model-invocation: true` in its SKILL frontmatter. Neither adapter transfers tool availability or proves behavior on another model.

## File Structure

```text
codex-config/
├── README.md
├── README.fr.md
├── THIRD_PARTY_NOTICES.md
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
│   ├── apply-profile.py
│   ├── copy-resources.py
│   └── test-instruction-tools.py
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

Vendored third-party skill notices are listed in `THIRD_PARTY_NOTICES.md`.
