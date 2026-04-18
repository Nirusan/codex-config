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

- `config/config.example.toml` → `~/.codex/config.toml` (ou `./.codex/config.toml`)
- Modèle public-safe uniquement : aucune vraie clé API ni chemin de projet personnel n'est versionné dans ce repo
- Modèle, approbations, sandbox, web search
- MCP servers (OpenAI Docs, Context7, Brave, Firecrawl, Supabase, Exa, n8n)
- Automation navigateur via la skill/CLI `dev-browser` plutôt qu’un browser MCP

### Skills

Les skills sont dans `skills/` et sont installés dans `~/.codex/skills/` ou `./.codex/skills/`.

Workflow principal :
- `refresh-context` → retrouver rapidement l’état d’un projet avant de reprendre
- `brainstorm` → transformer une idée floue en brief produit concret
- `prd` → écrire les requirements et le scope
- `tech-stack` → traduire les requirements en architecture
- `implementation-plan` → découper le travail en stories implémentables
- `next-task` → choisir le prochain morceau actionnable
- `implement` → exécuter l’unité de travail suivante
- `update-progress` → refléter ce qui a réellement été terminé

Debug, validation et qualité de livraison :
- `systematic-debugging` → debug orienté root cause pour les bugs flous ou flaky
- `validate` / `validate-quick` → validation complète ou rapide
- `completion-verification` → exiger une preuve fraîche avant d’annoncer que c’est prêt
- `validate-update-push` → wrap-up guidé de fin de tâche
- `git-add-commit-push` → finalisation Git explicite, uniquement quand tu la veux vraiment
- `security-check`, `db-check`, `seo-check`

Design et UI :
- `design-director` → cadrer une direction visuelle avant de construire
- `design-principles` → contraintes de design précises pour apps/dashboards
- `frontend-skill` → guide complémentaire pour composition, hiérarchie et retenue
- `taste-skill` → base premium pour générer une nouvelle UI frontend
- `redesign-skill` → auditer puis améliorer une interface existante
- `minimalist-skill` → surfaces produit plus calmes et éditoriales
- `soft-skill` → langage visuel plus doux et plus luxueux
- `output-skill` → pousse vers des sorties complètes sans placeholders
- `responsive-frontend-designs` → implémenter une UI depuis des screenshots ou références
- `dev-browser` → automation navigateur et validation visuelle
- `browser-based-games` → planifier et construire des jeux navigateur

Workflow frontend recommandé :
- Garde Gemini Design hors de la config par défaut. Utilise `gemini-design-mcp` uniquement quand tu veux explicitement cet outil dans un repo précis.
- Préfère `design-director` pour clarifier la direction, puis construis avec les skills frontend installées globalement.
- Utilise la famille Taste Skill comme couche principale d’exécution esthétique pour le frontend dans cette config.
- Garde `frontend-skill` comme guide complémentaire pour la composition de layout, la hiérarchie, l’enchaînement des sections et la retenue.
- Ne traite pas `taste-skill` et `frontend-skill` comme deux copilotes égaux du même passage : Taste mène, `frontend-skill` relit la composition ensuite.
- Laisse un `SKILL.md` local de Taste Skill ajouter des overrides spécifiques à un projet quand c’est utile.
- Bon mapping : `taste-skill` pour une nouvelle UI premium, `redesign-skill` pour une refonte, `minimalist-skill` pour des surfaces produit plus calmes, `output-skill` quand tu veux des sorties entièrement développées.

Utilitaires :
- `update-docs`, `sync-config`, `permissions-allow`, `humanizer`

### Setup automation navigateur

Ce repo utilise `dev-browser` pour l’automation navigateur en live au lieu d’un browser MCP.
`./install.sh` installe automatiquement la version vendoriée de [skills/dev-browser/SKILL.md](/Users/nirusan/Sites/codex-config/skills/dev-browser/SKILL.md) dans le dossier de skills Codex.

```bash
pnpm add -g dev-browser
dev-browser install
dev-browser --help
```

Installation manuelle au format Amp/Codex, si tu veux récupérer la skill upstream directement :

```bash
SKILLS_DIR=~/.codex/skills
mkdir -p "$SKILLS_DIR"
git clone https://github.com/sawyerhood/dev-browser /tmp/dev-browser-skill
cp -r /tmp/dev-browser-skill/skills/dev-browser "$SKILLS_DIR/dev-browser"
rm -rf /tmp/dev-browser-skill
```

### Comment les skills s’activent

Les skills peuvent être utilisées de deux façons :

- **Activation implicite** : Codex peut choisir automatiquement une skill si la demande correspond clairement à sa description.
- **Activation explicite** : tu peux appeler une skill directement avec `$nom-de-la-skill`, par exemple `$systematic-debugging` ou `$completion-verification`.

Ce repo garde volontairement certaines skills plus sensibles en **explicite uniquement**, notamment :
- `git-add-commit-push`
- `validate-update-push`

Pour le design, cette config traite maintenant la famille Taste Skill comme une partie du socle frontend global, tout en gardant les `SKILL.md` locaux comme meilleur endroit pour des contraintes spécifiques à un projet.

Ça permet de garder l’aide quotidienne fluide sans déclencher des actions Git ou de release par accident.

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

`./sync.sh` met à jour `config/config.example.toml`, pas ton vrai `config.toml` local. Relis toujours le template généré avant commit pour vérifier qu'il ne contient que des placeholders.

`./sync.sh` synchronise aussi les dossiers complets des skills, y compris les fichiers annexes :
- `agents/openai.yaml`
- `scripts/`
- `references/`
- `assets/`

## Structure du repo

```text
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

## Licence

MIT - Libre de forker et personnaliser.
