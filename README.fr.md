# Configuration Codex

Configuration Codex personnelle pour une expérience de dev cohérente sur toutes tes machines.

> ⚠️ **Attention** : Cette installation **écrase** ta configuration `~/.codex/`. Une sauvegarde est créée dans `~/.codex-backup-YYYYMMDD-HHMMSS/`.

## Prérequis

- **git** - pour cloner et synchroniser
- **curl** - pour l'installation en one-liner
- **bash** - shell (macOS/Linux/WSL)

## Installation rapide

### Niveau utilisateur (tous les projets de la machine)

```bash
# One-liner
curl -sSL https://raw.githubusercontent.com/Nirusan/codex-config/main/install.sh | bash

# Ou via clone
git clone https://github.com/Nirusan/codex-config.git
cd codex-config
./install.sh --user
```

### Niveau projet (uniquement le projet courant)

```bash
# One-liner
curl -sSL https://raw.githubusercontent.com/Nirusan/codex-config/main/install.sh | bash -s -- --project

# Ou via clone
git clone https://github.com/Nirusan/codex-config.git /tmp/codex-config
cd /path/to/your/project
/tmp/codex-config/install.sh --project
```

## Modes d’installation

| Mode | Flag | Cible | Usage |
|------|------|-------|-------|
| **User** | `--user` (par défaut) | `~/.codex/` | Machine perso, tous projets |
| **Project** | `--project` | `./.codex/` + `./AGENTS.md` | Config d’équipe, règles par repo |

### Options

| Flag | Description |
|------|-------------|
| `--yes` ou `-y` | Ignorer la confirmation (CI/Docker) |

---

## Contenu

### Instructions globales

- `config/AGENTS.md` → `~/.codex/AGENTS.md` (ou `./AGENTS.md` en mode projet)
- Conventions TypeScript/Next.js/nommage/style
- Réponses en français, code/docs en anglais

### Configuration Codex

- `config/config.toml` → `~/.codex/config.toml` (ou `./.codex/config.toml`)
- Modèle, approbations, sandbox, web search
- MCP servers (OpenAI Docs, Context7, Brave, Firecrawl, Supabase, Exa, Chrome DevTools, Gemini Design, n8n)

### Skills

Les skills sont dans `skills/` et sont installés dans `~/.codex/skills/` ou `./.codex/skills/`.

---

## Mise à jour

```bash
cd /path/to/codex-config
git pull
./install.sh
```

## Synchroniser la config locale vers le repo

```bash
cd /path/to/codex-config
./sync.sh
```

---

## Licence

MIT - Libre de forker et personnaliser.
