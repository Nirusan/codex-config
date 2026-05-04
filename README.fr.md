# Configuration Codex

Configuration Codex personnelle pour garder une expérience de dev cohérente sur toutes tes machines et tes stacks.

> Attention : l'installation niveau utilisateur met à jour `~/.codex/`. Une sauvegarde est créée dans `~/.codex-backup-YYYYMMDD-HHMMSS/`. Les installations de profils projet conservent le contenu humain de `AGENTS.md` hors blocs balisés.

## Prérequis

- **git** - cloner et synchroniser
- **curl** - installation one-liner
- **bash** - shell (macOS/Linux/WSL)
- **python3** - mise à jour idempotente des profils projet

## Installation Rapide

### Niveau utilisateur (tous les projets de la machine)

```bash
# One-liner
curl -sSL https://raw.githubusercontent.com/Nirusan/codex-config/main/install.sh | bash

# Ou via clone
git clone https://github.com/Nirusan/codex-config.git
cd codex-config
./install.sh --user
```

### Profils niveau projet

```bash
# Config projet neutre
curl -sSL https://raw.githubusercontent.com/Nirusan/codex-config/main/install.sh | bash -s -- --project

# Profil projet Next.js
curl -sSL https://raw.githubusercontent.com/Nirusan/codex-config/main/install.sh | bash -s -- --project --profile next

# Profil projet Expo / React Native
curl -sSL https://raw.githubusercontent.com/Nirusan/codex-config/main/install.sh | bash -s -- --project --profile expo
```

Depuis un clone local :

```bash
git clone https://github.com/Nirusan/codex-config.git /tmp/codex-config
cd /path/to/your/project
/tmp/codex-config/install.sh --project --profile next
```

Le mode one-liner récupère une copie temporaire complète du repo avant l'installation. Les ressources imbriquées des skills, comme `agents/`, `scripts/`, `references/` et `assets/`, sont donc préservées comme avec une installation depuis clone local.

Pour un monorepo, cible un dossier d'app précis :

```bash
/tmp/codex-config/install.sh --project --profile next --target apps/web
/tmp/codex-config/install.sh --project --profile expo --target apps/mobile
```

## Modes D'installation

| Mode | Flag | Cible | Usage |
|------|------|-------|-------|
| User | `--user` (par défaut) | `~/.codex/` | Machine perso, tous projets |
| Project | `--project` | `./.codex/` + `./AGENTS.md` | Config neutre d'équipe ou de repo |
| Project profile | `--project --profile next\|expo` | `.codex/` cible + bloc profil dans `AGENTS.md` | Qualité spécifique à une stack |

Options :

| Flag | Description |
|------|-------------|
| `--yes` ou `-y` | Ignorer la confirmation |
| `--profile next` | Appliquer ou rafraîchir le profil Codex Next.js |
| `--profile expo` | Appliquer ou rafraîchir le profil Codex Expo / React Native |
| `--target path` | Appliquer la config projet à un dossier précis |

Overrides pour source distante :

| Env var | Description |
|---------|-------------|
| `SOURCE_REPO_URL` | Repo Git utilisé par les installations one-liner distantes |
| `SOURCE_BRANCH` | Branche à cloner ou télécharger, par défaut `main` |
| `ARCHIVE_URL` | Tarball de fallback si Git clone n'est pas disponible |

## Profils Projet

Ce repo utilise une configuration en couches :

- `config/AGENTS.md` est le socle global neutre.
- `profiles/next/AGENTS.md` contient les règles Next.js / React web.
- `profiles/expo/AGENTS.md` contient les règles Expo / React Native.
- `scripts/apply-profile.py` insère ou rafraîchit un bloc profil dans le `AGENTS.md` projet.

Les installations de profil sont idempotentes et préservent tout ce qui est hors marqueurs :

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

Dans Codex, utilise `$setup-next` ou `$setup-expo` pour appliquer le bon profil et obtenir un audit court de la config projet.

## Contenu

### Instructions Globales

- Conventions neutres TypeScript, nommage, style, validation, docs et routing de skills
- Réponses en français, code/docs/config interne en anglais
- Règles spécifiques aux stacks sorties du socle global

### Configuration Codex

- `config/config.example.toml` -> `~/.codex/config.toml` ou `./.codex/config.toml`
- Template public-safe uniquement : aucune vraie clé API ni chemin personnel
- MCP servers pour OpenAI Docs, Context7, Brave, Firecrawl, Supabase, Exa, n8n
- Automation navigateur via la skill/CLI `dev-browser` plutôt qu'un browser MCP

### Skills

Workflow principal :
- `refresh-context` -> retrouver rapidement l'état d'un projet avant de reprendre
- `brainstorm`, `prd`, `tech-stack`, `implementation-plan` -> transformer une idée en plan buildable
- `next-task`, `implement`, `update-progress` -> choisir, exécuter et documenter le travail
- `setup-next`, `setup-expo` -> appliquer et auditer les profils projet par stack

Debug, validation et livraison :
- `systematic-debugging` -> debug orienté root cause
- `validate`, `validate-quick`, `completion-verification` -> checks de readiness
- `validate-update-push`, `git-add-commit-push` -> workflows de fin explicites
- `security-check`, `db-check`, `seo-check`

Design et UI :
- `design-director`, `design-principles`, `frontend-skill`
- `taste-skill`, `redesign-skill`, `minimalist-skill`, `soft-skill`, `output-skill`
- `responsive-frontend-designs`, `dev-browser`, `browser-based-games`

Workflow frontend recommandé :
- Garder Gemini Design hors de la config par défaut sauf demande explicite.
- Appliquer `$setup-next` pour les projets Next.js sérieux et `$setup-expo` pour les projets Expo / React Native sérieux.
- Utiliser Taste Skill comme couche principale d'exécution esthétique et `frontend-skill` comme check secondaire de composition.
- Laisser les `SKILL.md` locaux ajouter les overrides spécifiques au projet.

## Setup Automation Navigateur

Ce repo utilise `dev-browser` pour l'automation navigateur live.

```bash
pnpm add -g dev-browser
dev-browser install
dev-browser --help
```

## Mise A Jour

```bash
cd /path/to/codex-config
git pull
./install.sh
```

## Synchroniser La Config Locale Vers Le Repo

```bash
cd /path/to/codex-config
./sync.sh
```

`./sync.sh` met à jour `config/config.example.toml`, synchronise les dossiers complets des skills, et synchronise aussi `profiles/` plus `scripts/apply-profile.py` quand ils existent dans `~/.codex/`. Relis la config générée avant commit.

## Structure Du Repo

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

## Licence

MIT - Libre de forker et personnaliser.
