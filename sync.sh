#!/bin/bash
set -euo pipefail

# Copy personal instructions/resources into this checkout for review. Never stage, commit or push.
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SOURCE_CODEX_DIR="${CODEX_HOME:-$HOME/.codex}"
if [[ $# -gt 0 ]]; then
  if [[ $# -ne 2 || "$1" != "--source" ]]; then
    echo "Usage: sync.sh [--source /path/to/codex-config]" >&2
    exit 1
  fi
  SOURCE_CODEX_DIR="$2"
fi

python3 "$SCRIPT_DIR/scripts/copy-resources.py" sync "$SOURCE_CODEX_DIR" "$SCRIPT_DIR"

# Back up Codex memories to a SEPARATE PRIVATE repo (memory never lands in this public one).
# Decision 2026-10-20: memories hold personal and business notes; the visibility check
# refuses any clone whose GitHub repo is not private. memories/.git is Codex's own local
# baseline and the *.sqlite stores are runtime state, so neither is copied.
MEMORY_REPO="${CODEX_MEMORY_REPO:-$HOME/Sites/codex-memory}"
echo "==> Syncing Codex memories → $MEMORY_REPO..."
if [[ ! -d "$MEMORY_REPO/.git" ]]; then
  echo "    ⚠ $MEMORY_REPO is not a git clone, skipping (gh repo clone Nirusan/codex-memory $MEMORY_REPO)"
elif [[ "$(cd "$MEMORY_REPO" && gh repo view --json visibility -q .visibility 2>/dev/null)" != "PRIVATE" ]]; then
  echo "    ⚠ $MEMORY_REPO is not a verified PRIVATE GitHub repo, skipping"
else
  if [[ -d "$SOURCE_CODEX_DIR/memories" ]]; then
    rsync -a --delete --exclude '.git' --exclude '.DS_Store' "$SOURCE_CODEX_DIR/memories/" "$MEMORY_REPO/memories/"
    echo "    ✓ memories/"
  fi
  if [[ -f "$SOURCE_CODEX_DIR/memory.md" ]]; then
    cp "$SOURCE_CODEX_DIR/memory.md" "$MEMORY_REPO/memory.md"
    echo "    ✓ memory.md"
  fi
  echo "    Commit and push from $MEMORY_REPO when ready."
fi
