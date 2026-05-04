#!/bin/bash
set -e

# Codex Configuration Installer
# Usage:
#   ./install.sh                                      # Install user-level config
#   ./install.sh --user                               # Install user-level config (~/.codex/)
#   ./install.sh --project                            # Install project-level neutral config
#   ./install.sh --project --profile next             # Apply the Next profile to the current project
#   ./install.sh --project --profile expo             # Apply the Expo profile to the current project
#   ./install.sh --project --profile next --target apps/web

REPO_URL="${REPO_URL:-https://raw.githubusercontent.com/Nirusan/codex-config/main}"
SOURCE_REPO_URL="${SOURCE_REPO_URL:-https://github.com/Nirusan/codex-config.git}"
SOURCE_BRANCH="${SOURCE_BRANCH:-main}"
ARCHIVE_URL="${ARCHIVE_URL:-https://github.com/Nirusan/codex-config/archive/refs/heads/$SOURCE_BRANCH.tar.gz}"
REMOTE_SOURCE_DIR=""

cleanup_remote_source() {
  if [[ -n "$REMOTE_SOURCE_DIR" && -d "$REMOTE_SOURCE_DIR" ]]; then
    rm -rf "$REMOTE_SOURCE_DIR"
  fi
}
trap cleanup_remote_source EXIT

usage() {
  echo "Codex Configuration Installer"
  echo ""
  echo "Usage:"
  echo "  ./install.sh                                      Install user-level config"
  echo "  ./install.sh --user                               Install user-level config (~/.codex/)"
  echo "  ./install.sh --project                            Install project-level neutral config"
  echo "  ./install.sh --project --profile next             Apply Next profile to the current project"
  echo "  ./install.sh --project --profile expo             Apply Expo profile to the current project"
  echo "  ./install.sh --project --profile next --target apps/web"
  echo "  ./install.sh --yes|-y                             Skip confirmation prompt"
  echo ""
  echo "Profiles:"
  echo "  next   Next.js / React web projects"
  echo "  expo   Expo / React Native projects"
}

INSTALL_MODE="user"
SKIP_CONFIRM="false"
PROFILE=""
TARGET_PATH="."

while [[ $# -gt 0 ]]; do
  case "$1" in
    --project)
      INSTALL_MODE="project"
      shift
      ;;
    --user)
      INSTALL_MODE="user"
      shift
      ;;
    --profile)
      shift
      if [[ $# -eq 0 ]]; then
        echo "error: --profile requires next or expo" >&2
        exit 1
      fi
      PROFILE="$1"
      shift
      ;;
    --profile=*)
      PROFILE="${1#*=}"
      shift
      ;;
    --target)
      shift
      if [[ $# -eq 0 ]]; then
        echo "error: --target requires a path" >&2
        exit 1
      fi
      TARGET_PATH="$1"
      shift
      ;;
    --target=*)
      TARGET_PATH="${1#*=}"
      shift
      ;;
    --yes|-y)
      SKIP_CONFIRM="true"
      shift
      ;;
    --help|-h)
      usage
      exit 0
      ;;
    *)
      echo "error: unknown option: $1" >&2
      usage
      exit 1
      ;;
  esac
done

if [[ -n "$PROFILE" && "$PROFILE" != "next" && "$PROFILE" != "expo" ]]; then
  echo "error: --profile must be either next or expo" >&2
  exit 1
fi

if [[ -n "$PROFILE" && "$INSTALL_MODE" != "project" ]]; then
  echo "error: --profile requires --project" >&2
  exit 1
fi

if [[ "$TARGET_PATH" != "." && "$INSTALL_MODE" != "project" ]]; then
  echo "error: --target requires --project" >&2
  exit 1
fi

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
if [[ -f "$SCRIPT_DIR/config/config.example.toml" ]]; then
  LOCAL_INSTALL=true
else
  LOCAL_INSTALL=false
fi

prepare_remote_source() {
  REMOTE_SOURCE_DIR="$(mktemp -d)"
  local repo_dir="$REMOTE_SOURCE_DIR/repo"

  if command -v git >/dev/null 2>&1; then
    echo "==> Fetching complete remote config from Git..."
    if git clone --depth 1 --branch "$SOURCE_BRANCH" "$SOURCE_REPO_URL" "$repo_dir" >/dev/null 2>&1; then
      SCRIPT_DIR="$repo_dir"
      LOCAL_INSTALL=true
      return
    fi
    echo "    Git clone failed; trying archive download..."
  fi

  if command -v curl >/dev/null 2>&1 && command -v tar >/dev/null 2>&1; then
    echo "==> Fetching complete remote config archive..."
    mkdir -p "$REMOTE_SOURCE_DIR/archive"
    curl -fsSL "$ARCHIVE_URL" -o "$REMOTE_SOURCE_DIR/source.tar.gz"
    tar -xzf "$REMOTE_SOURCE_DIR/source.tar.gz" -C "$REMOTE_SOURCE_DIR/archive"
    repo_dir="$(find "$REMOTE_SOURCE_DIR/archive" -mindepth 1 -maxdepth 1 -type d | head -n 1)"
    if [[ -n "$repo_dir" && -f "$repo_dir/config/config.example.toml" ]]; then
      SCRIPT_DIR="$repo_dir"
      LOCAL_INSTALL=true
      return
    fi
  fi

  echo "error: could not fetch the complete remote config repo" >&2
  echo "       Set SOURCE_REPO_URL or ARCHIVE_URL if you use a fork." >&2
  exit 1
}

if [[ "$INSTALL_MODE" == "project" ]]; then
  if [[ ! -d "$TARGET_PATH" ]]; then
    echo "error: target directory does not exist: $TARGET_PATH" >&2
    exit 1
  fi
  TARGET_DIR="$(cd "$TARGET_PATH" && pwd)"
  CODEX_DIR="$TARGET_DIR/.codex"
  AGENTS_TARGET="$TARGET_DIR/AGENTS.md"
  BACKUP_DIR="$TARGET_DIR/.codex-backup-$(date +%Y%m%d-%H%M%S)"
  echo "==> Installing Codex configuration (PROJECT-level)..."
  echo "    Target: $TARGET_DIR"
else
  TARGET_DIR="$HOME"
  CODEX_DIR="$HOME/.codex"
  AGENTS_TARGET="$CODEX_DIR/AGENTS.md"
  BACKUP_DIR="$HOME/.codex-backup-$(date +%Y%m%d-%H%M%S)"
  echo "==> Installing Codex configuration (USER-level)..."
  echo "    Target: ~/.codex/"
fi

if [[ "$LOCAL_INSTALL" == true ]]; then
  echo "==> Installing from local clone..."
else
  echo "==> Installing from remote..."
  prepare_remote_source
fi

# Backup existing config if present.
if [[ ( -d "$CODEX_DIR" && "$(ls -A "$CODEX_DIR" 2>/dev/null)" ) || -f "$AGENTS_TARGET" ]]; then
  echo ""
  echo "WARNING / ATTENTION"
  echo "────────────────────────────────────────"
  echo "EN: An existing Codex config was found."
  echo "    This script may update your Codex configuration."
  echo "    A backup will be created at: $BACKUP_DIR"
  echo ""
  echo "FR: Une configuration Codex existante a été trouvée."
  echo "    Ce script peut mettre à jour votre configuration Codex."
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

install_file() {
  local src="$1"
  local dest="$2"
  rm -f "$dest" 2>/dev/null || true
  mkdir -p "$(dirname "$dest")"

  if [[ "$LOCAL_INSTALL" == true ]]; then
    cp "$SCRIPT_DIR/$src" "$dest"
  else
    # Fallback for unexpected partial remote installs. Normal remote installs
    # fetch the complete repo first, then use the local-copy path above.
    curl -fsSL "$REPO_URL/$src" -o "$dest"
  fi
}

install_optional_file() {
  local src="$1"
  local dest="$2"
  rm -f "$dest" 2>/dev/null || true
  mkdir -p "$(dirname "$dest")"

  if [[ "$LOCAL_INSTALL" == true ]]; then
    if [[ -f "$SCRIPT_DIR/$src" ]]; then
      cp "$SCRIPT_DIR/$src" "$dest"
    fi
  else
    # Fallback for unexpected partial remote installs. Normal remote installs
    # fetch the complete repo first, then use the local-copy path above.
    curl -fsSL "$REPO_URL/$src" -o "$dest" 2>/dev/null || rm -f "$dest"
  fi
}

extract_mcp_sections() {
  local file="$1"
  awk '
    /^\[mcp_servers\.chrome-devtools(\.|$)/ { keep=0; skip_legacy=1; next }
    /^\[mcp_servers\.gemini-design-mcp(\.|$)/ { keep=0; skip_gemini=1; next }
    /^\[/ && skip_legacy && $0 !~ /^\[mcp_servers\.chrome-devtools(\.|$)/ { skip_legacy=0 }
    /^\[/ && skip_gemini && $0 !~ /^\[mcp_servers\.gemini-design-mcp(\.|$)/ { skip_gemini=0 }
    skip_legacy || skip_gemini { next }
    /^\[mcp_servers(\.|$)/ && !skip_legacy { keep=1 }
    /^\[/ && $0 !~ /^\[mcp_servers(\.|$)/ { keep=0 }
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

install_support_files() {
  echo "==> Installing profiles and helpers..."
  install_file "scripts/apply-profile.py" "$CODEX_DIR/scripts/apply-profile.py"
  chmod +x "$CODEX_DIR/scripts/apply-profile.py"

  for profile_name in next expo; do
    install_file "profiles/$profile_name/AGENTS.md" "$CODEX_DIR/profiles/$profile_name/AGENTS.md"
  done
}

apply_project_profile() {
  local profile_name="$1"
  echo "==> Applying project profile: $profile_name"
  python3 "$CODEX_DIR/scripts/apply-profile.py" \
    --profile "$profile_name" \
    --target "$TARGET_DIR" \
    --profiles-dir "$CODEX_DIR/profiles"
}

install_skill() {
  local skill_name="$1"
  local skill_src="$SCRIPT_DIR/skills/$skill_name"
  local skill_dest="$CODEX_DIR/skills/$skill_name"
  mkdir -p "$skill_dest"

  if [[ "$LOCAL_INSTALL" == true ]]; then
    if [[ -d "$skill_src" ]]; then
      cp -R "$skill_src/." "$skill_dest/"
    fi
  else
    install_file "skills/$skill_name/SKILL.md" "$skill_dest/SKILL.md"
    install_optional_file "skills/$skill_name/agents/openai.yaml" "$skill_dest/agents/openai.yaml"
  fi
}

echo "==> Copying config files..."
install_support_files

existing_config="$(mktemp)"
if [[ -f "$CODEX_DIR/config.toml" ]]; then
  cp "$CODEX_DIR/config.toml" "$existing_config"
fi
install_file "config/config.example.toml" "$CODEX_DIR/config.toml"
if [[ -s "$existing_config" ]]; then
  merge_mcp_sections "$CODEX_DIR/config.toml" "$existing_config"
fi
rm -f "$existing_config"

if [[ "$INSTALL_MODE" == "project" ]]; then
  if [[ -n "$PROFILE" ]]; then
    apply_project_profile "$PROFILE"
  else
    install_file "config/AGENTS.md" "$AGENTS_TARGET"
  fi
else
  install_file "config/AGENTS.md" "$AGENTS_TARGET"
fi

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
  "minimalist-skill"
  "next-task"
  "output-skill"
  "dev-browser"
  "permissions-allow"
  "prd"
  "refresh-context"
  "redesign-skill"
  "responsive-frontend-designs"
  "security-check"
  "seo-check"
  "setup-expo"
  "setup-next"
  "soft-skill"
  "systematic-debugging"
  "taste-skill"
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

echo ""
echo "==> Installation complete!"
echo ""
if [[ "$INSTALL_MODE" == "project" ]]; then
  echo "Installed (PROJECT-level):"
  echo "  - $TARGET_DIR/.codex/config.toml"
  echo "  - $TARGET_DIR/.codex/skills/*"
  echo "  - $TARGET_DIR/.codex/profiles/*"
  echo "  - $TARGET_DIR/.codex/scripts/apply-profile.py"
  if [[ -n "$PROFILE" ]]; then
    echo "  - $TARGET_DIR/AGENTS.md profile block: $PROFILE"
  else
    echo "  - $TARGET_DIR/AGENTS.md"
  fi
else
  echo "Installed (USER-level):"
  echo "  - ~/.codex/AGENTS.md"
  echo "  - ~/.codex/config.toml"
  echo "  - ~/.codex/skills/*"
  echo "  - ~/.codex/profiles/*"
  echo "  - ~/.codex/scripts/apply-profile.py"
fi

echo ""
echo "Next steps:"
if [[ "$INSTALL_MODE" == "user" ]]; then
  echo "  - Edit ~/.codex/config.toml to add API keys for MCP servers"
  echo "  - Use \$setup-next or \$setup-expo inside projects when you want a project profile"
else
  echo "  - Review $TARGET_DIR/AGENTS.md"
fi

echo ""
echo "Note: Restart Codex for changes to take effect."
