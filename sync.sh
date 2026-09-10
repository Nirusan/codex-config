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
