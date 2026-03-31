#!/bin/bash
set -e

# Codex Configuration Installer
# Usage:
#   ./install.sh              # Install user-level config (default)
#   ./install.sh --user       # Install user-level config (~/.codex/)
#   ./install.sh --project    # Install project-level config (./.codex/ + ./AGENTS.md)

REPO_URL="${REPO_URL:-https://raw.githubusercontent.com/Nirusan/codex-config/main}"

INSTALL_MODE="user"
SKIP_CONFIRM="false"
for arg in "$@"; do
  case $arg in
    --project)
      INSTALL_MODE="project"
      shift
      ;;
    --user)
      INSTALL_MODE="user"
      shift
      ;;
    --yes|-y)
      SKIP_CONFIRM="true"
      shift
      ;;
    --help|-h)
      echo "Codex Configuration Installer"
      echo ""
      echo "Usage:"
      echo "  ./install.sh              Install user-level config (default)"
      echo "  ./install.sh --user       Install user-level config (~/.codex/)"
      echo "  ./install.sh --project    Install project-level config (./.codex/ + ./AGENTS.md)"
      echo "  ./install.sh --yes|-y     Skip confirmation prompt"
      echo ""
      echo "User-level:    Applies to ALL projects on this machine"
      echo "Project-level: Applies only to the current project"
      exit 0
      ;;
  esac
done

if [[ "$INSTALL_MODE" == "project" ]]; then
  CODEX_DIR="./.codex"
  AGENTS_TARGET="./AGENTS.md"
  BACKUP_DIR="./.codex-backup-$(date +%Y%m%d-%H%M%S)"
  echo "==> Installing Codex configuration (PROJECT-level)..."
  echo "    Target: $(pwd)/.codex/"
else
  CODEX_DIR="$HOME/.codex"
  AGENTS_TARGET="$CODEX_DIR/AGENTS.md"
  BACKUP_DIR="$HOME/.codex-backup-$(date +%Y%m%d-%H%M%S)"
  echo "==> Installing Codex configuration (USER-level)..."
  echo "    Target: ~/.codex/"
fi

# Backup existing config if present
if [[ ( -d "$CODEX_DIR" && "$(ls -A "$CODEX_DIR" 2>/dev/null)" ) || -f "$AGENTS_TARGET" ]]; then
  echo ""
  echo "⚠️  WARNING / ATTENTION"
  echo "────────────────────────────────────────"
  echo "EN: An existing Codex config was found."
  echo "    This script will OVERWRITE your current configuration."
  echo "    A backup will be created at: $BACKUP_DIR"
  echo ""
  echo "FR: Une configuration Codex existante a été trouvée."
  echo "    Ce script va ÉCRASER votre configuration actuelle."
  echo "    Une sauvegarde sera créée dans : $BACKUP_DIR"
  echo "────────────────────────────────────────"
  echo ""
  if [[ "$SKIP_CONFIRM" != "true" ]]; then
    read -p "Continue? / Continuer ? [y/N] " -n 1 -r < /dev/tty
    echo ""
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
      echo "Aborted. / Abandon."
      exit 1
    fi
  else
    echo "(--yes flag: skipping confirmation / option --yes : confirmation ignorée)"
  fi
  echo "==> Backing up existing config to $BACKUP_DIR..."
  mkdir -p "$BACKUP_DIR"
  if [[ -d "$CODEX_DIR" ]]; then
    cp -rP "$CODEX_DIR" "$BACKUP_DIR/" || true
  fi
  if [[ -f "$AGENTS_TARGET" ]]; then
    cp -P "$AGENTS_TARGET" "$BACKUP_DIR/AGENTS.md" || true
  fi
fi

mkdir -p "$CODEX_DIR/skills"

# Remove the legacy browser skill after the rename to dev-browser.
if [[ -d "$CODEX_DIR/skills/playwright" ]]; then
  rm -rf "$CODEX_DIR/skills/playwright"
fi

# Detect if running from local clone or remote
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
if [[ -f "$SCRIPT_DIR/config/config.example.toml" ]]; then
  echo "==> Installing from local clone..."
  LOCAL_INSTALL=true
else
  echo "==> Installing from remote..."
  LOCAL_INSTALL=false
fi

install_file() {
  local src="$1"
  local dest="$2"
  rm -f "$dest" 2>/dev/null || true

  if [[ "$LOCAL_INSTALL" == true ]]; then
    cp "$SCRIPT_DIR/$src" "$dest"
  else
    curl -sSL "$REPO_URL/$src" -o "$dest"
  fi
}

extract_mcp_sections() {
  local file="$1"
  awk '
    /^\[mcp_servers\.chrome-devtools(\.|$)/ { keep=0; skip_legacy=1; next }
    /^\[/ && skip_legacy && $0 !~ /^\[mcp_servers\.chrome-devtools(\.|$)/ { skip_legacy=0 }
    /^\[mcp_servers(\.|$)/ && !skip_legacy { keep=1 }
    /^\[/ && $0 !~ /^\[mcp_servers(\.|$)/ { keep=0 }
    skip_legacy { next }
    keep { print }
  ' "$file"
}

strip_mcp_sections() {
  local file="$1"
  awk '
    /^\[mcp_servers(\.|$)/ { skip=1; next }
    /^\[/ && $0 !~ /^\[mcp_servers(\.|$)/ { skip=0 }
    !skip { print }
  ' "$file"
}

merge_mcp_sections() {
  local new_file="$1"
  local old_file="$2"
  local tmp_new
  local tmp_mcp
  tmp_new="$(mktemp)"
  tmp_mcp="$(mktemp)"

  extract_mcp_sections "$old_file" > "$tmp_mcp"
  if [[ -s "$tmp_mcp" ]]; then
    strip_mcp_sections "$new_file" > "$tmp_new"
    {
      cat "$tmp_new"
      echo ""
      cat "$tmp_mcp"
    } > "$new_file"
  fi

  rm -f "$tmp_new" "$tmp_mcp"
}

install_skill() {
  local skill_name="$1"
  mkdir -p "$CODEX_DIR/skills/$skill_name"
  if [[ "$LOCAL_INSTALL" == true ]]; then
    cp -R "$SCRIPT_DIR/skills/$skill_name/"* "$CODEX_DIR/skills/$skill_name/" 2>/dev/null || true
  else
    install_file "skills/$skill_name/SKILL.md" "$CODEX_DIR/skills/$skill_name/SKILL.md"
  fi
}

# Install config files
echo "==> Copying config files..."
if [[ "$INSTALL_MODE" == "project" ]]; then
  install_file "config/AGENTS.md" "$AGENTS_TARGET"
  existing_config="$(mktemp)"
  if [[ -f "$CODEX_DIR/config.toml" ]]; then
    cp "$CODEX_DIR/config.toml" "$existing_config"
  fi
  install_file "config/config.example.toml" "$CODEX_DIR/config.toml"
  if [[ -s "$existing_config" ]]; then
    merge_mcp_sections "$CODEX_DIR/config.toml" "$existing_config"
  fi
  rm -f "$existing_config"
else
  install_file "config/AGENTS.md" "$AGENTS_TARGET"
  existing_config="$(mktemp)"
  if [[ -f "$CODEX_DIR/config.toml" ]]; then
    cp "$CODEX_DIR/config.toml" "$existing_config"
  fi
  install_file "config/config.example.toml" "$CODEX_DIR/config.toml"
  if [[ -s "$existing_config" ]]; then
    merge_mcp_sections "$CODEX_DIR/config.toml" "$existing_config"
  fi
  rm -f "$existing_config"
fi

# Install skills
echo "==> Installing skills..."
SKILLS=(
  "brainstorm"
  "db-check"
  "design-director"
  "design-principles"
  "completion-verification"
  "frontend-skill"
  "git-add-commit-push"
  "humanizer"
  "implement"
  "implementation-plan"
  "next-task"
  "dev-browser"
  "permissions-allow"
  "prd"
  "refresh-context"
  "responsive-frontend-designs"
  "security-check"
  "seo-check"
  "systematic-debugging"
  "sync-config"
  "tech-stack"
  "update-docs"
  "update-progress"
  "validate"
  "validate-quick"
  "validate-update-push"
  "worktree-setup"
  "browser-based-games"
)
for skill in "${SKILLS[@]}"; do
  install_skill "$skill"
done

# Summary
echo ""
echo "==> Installation complete!"
echo ""
if [[ "$INSTALL_MODE" == "project" ]]; then
  echo "Installed (PROJECT-level):"
  echo "  - ./AGENTS.md"
  echo "  - ./.codex/config.toml"
  echo "  - ./.codex/skills/*"
else
  echo "Installed (USER-level):"
  echo "  - ~/.codex/AGENTS.md"
  echo "  - ~/.codex/config.toml"
  echo "  - ~/.codex/skills/*"
fi

echo ""
echo "Next steps:"
if [[ "$INSTALL_MODE" == "user" ]]; then
  echo "  - Edit ~/.codex/config.toml to add API keys for MCP servers"
else
  echo "  - Edit ./.codex/config.toml to add API keys for MCP servers"
fi

echo ""
echo "Note: Restart Codex for changes to take effect."
