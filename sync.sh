#!/bin/bash
set -e

# Sync local ~/.codex/ config back to this repo
# Usage: ./sync.sh

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CODEX_DIR="$HOME/.codex"

echo "==> Syncing ~/.codex/ → repo..."

# Sync AGENTS.md
if [[ -f "$CODEX_DIR/AGENTS.md" ]]; then
  cp "$CODEX_DIR/AGENTS.md" "$SCRIPT_DIR/config/AGENTS.md"
  echo "    ✓ config/AGENTS.md"
fi

# Sync config.toml
if [[ -f "$CODEX_DIR/config.toml" ]]; then
  cp "$CODEX_DIR/config.toml" "$SCRIPT_DIR/config/config.toml"
  echo "    ✓ config/config.toml"
fi

# Sync skills (all subdirectories)
if [[ -d "$CODEX_DIR/skills" ]]; then
  for skill_dir in "$CODEX_DIR/skills"/*/; do
    if [[ -d "$skill_dir" ]]; then
      skill_name=$(basename "$skill_dir")
      mkdir -p "$SCRIPT_DIR/skills/$skill_name"
      if [[ -f "$skill_dir/SKILL.md" ]]; then
        cp "$skill_dir/SKILL.md" "$SCRIPT_DIR/skills/$skill_name/SKILL.md"
        echo "    ✓ skills/$skill_name/SKILL.md"
      fi
      for extra_file in "$skill_dir"*; do
        if [[ -f "$extra_file" && "$(basename "$extra_file")" != "SKILL.md" ]]; then
          cp "$extra_file" "$SCRIPT_DIR/skills/$skill_name/"
          echo "    ✓ skills/$skill_name/$(basename "$extra_file")"
        fi
      done
      if [[ -d "$skill_dir/scripts" ]]; then
        mkdir -p "$SCRIPT_DIR/skills/$skill_name/scripts"
        cp -r "$skill_dir/scripts/"* "$SCRIPT_DIR/skills/$skill_name/scripts/" 2>/dev/null || true
        echo "    ✓ skills/$skill_name/scripts/"
      fi
    fi
  done
fi

echo ""
echo "==> Sync complete!"
echo ""
echo "Next steps:"
echo "  cd $SCRIPT_DIR"
echo "  git status"
echo "  git add -A && git commit -m 'sync config' && git push"
echo ""
echo "Reminder: Review config.toml for any secrets before pushing."
