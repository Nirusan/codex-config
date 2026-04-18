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
- MCP server templates (OpenAI Docs, Context7, Brave, Firecrawl, Supabase, Exa, n8n)
- Browser automation via the `dev-browser` skill/CLI instead of a browser MCP server

### Skills

All skills live in `skills/` and are installed to `~/.codex/skills/` or `./.codex/skills/`.

Core workflow:
- `refresh-context` → recover project state before resuming work
- `brainstorm` → turn a vague idea into a concrete product brief
- `prd` → write requirements and scope
- `tech-stack` → translate requirements into architecture
- `implementation-plan` → break work into implementable stories
- `next-task` → select the next actionable chunk
- `implement` → execute the next concrete unit of work
- `update-progress` → reflect what was actually completed

Debugging, validation, and release hygiene:
- `systematic-debugging` → root-cause-first debugging for flaky or non-obvious issues
- `validate` / `validate-quick` → fast or full verification
- `completion-verification` → evidence-before-claims before saying work is ready
- `validate-update-push` → guided end-of-task wrap-up
- `git-add-commit-push` → explicit Git finalization only when you really want it
- `security-check`, `db-check`, `seo-check`

Design and UI:
- `design-director` → define a visual direction before building
- `design-principles` → precise app/dashboard design constraints
- `frontend-skill` → stronger art direction for web/app UI
- `taste-skill` → premium frontend generation defaults for new UI work
- `redesign-skill` → audit and upgrade an existing interface
- `minimalist-skill` → calmer editorial/product surfaces
- `soft-skill` → softer premium/luxury visual language
- `output-skill` → pushes for complete, no-placeholder frontend output
- `responsive-frontend-designs` → implement UI from screenshots or references
- `dev-browser` → browser automation and visual checking
- `browser-based-games` → plan and build browser games

Recommended frontend workflow:
- Keep Gemini Design out of the default config. Use `gemini-design-mcp` only when you explicitly want that tool in a specific repo.
- Prefer `design-director` to clarify direction, then build with the globally installed frontend skills.
- Use the Taste Skill family as the default aesthetic layer for frontend work in this config.
- Let a repo-local `SKILL.md` from Taste Skill add project-specific overrides when needed.
- Good pairing: `taste-skill` for new premium UI, `redesign-skill` for upgrades, `minimalist-skill` for calmer product surfaces, `output-skill` when you want fully expanded outputs.

Utilities:
- `update-docs`, `sync-config`, `permissions-allow`, `humanizer`

### Browser Automation Setup

This repo uses `dev-browser` for live browser automation instead of a browser MCP server.
`./install.sh` installs the vendored [skills/dev-browser/SKILL.md](/Users/nirusan/Sites/codex-config/skills/dev-browser/SKILL.md) into your Codex skills directory automatically.

```bash
pnpm add -g dev-browser
dev-browser install
dev-browser --help
```

Official manual Amp/Codex-style skill install, if you want the upstream skill directly:

```bash
SKILLS_DIR=~/.codex/skills
mkdir -p "$SKILLS_DIR"
git clone https://github.com/sawyerhood/dev-browser /tmp/dev-browser-skill
cp -r /tmp/dev-browser-skill/skills/dev-browser "$SKILLS_DIR/dev-browser"
rm -rf /tmp/dev-browser-skill
```

### How Skills Are Invoked

Skills can be used in two ways:

- **Implicit invocation**: Codex can choose a skill automatically when your request clearly matches the skill description.
- **Explicit invocation**: you can call a skill directly with `$skill-name`, for example `$systematic-debugging` or `$completion-verification`.

This repo intentionally keeps some higher-risk skills **explicit-only**, especially:
- `git-add-commit-push`
- `validate-update-push`

For design guidance, this config now treats the Taste Skill family as part of the default global frontend stack, while repo-local `SKILL.md` files remain the best way to add project-specific design constraints.

That keeps everyday help automatic while avoiding accidental Git or release actions.

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

`./sync.sh` also syncs full skill directories, including nested metadata and helper files such as:
- `agents/openai.yaml`
- `scripts/`
- `references/`
- `assets/`

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
    ├── brainstorm/
    │   ├── SKILL.md
    │   └── agents/openai.yaml
    ├── completion-verification/
    │   ├── SKILL.md
    │   └── agents/openai.yaml
    ├── dev-browser/
    │   ├── SKILL.md
    │   └── agents/openai.yaml
    ├── responsive-frontend-designs/
    │   └── SKILL.md
    ├── systematic-debugging/
    │   ├── SKILL.md
    │   └── agents/openai.yaml
    ├── worktree-setup/
    │   ├── SKILL.md
    │   └── agents/openai.yaml
    └── ...
```

---

## License

MIT - Feel free to fork and customize.
