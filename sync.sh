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

# Sync config template (public-safe, redacted)
if [[ -f "$CODEX_DIR/config.toml" ]]; then
  python3 - "$CODEX_DIR/config.toml" "$SCRIPT_DIR/config/config.example.toml" <<'PY'
from pathlib import Path
import re
import sys

src = Path(sys.argv[1])
dest = Path(sys.argv[2])

text = src.read_text()
lines = []
skip_project_block = False
skip_legacy_browser_block = False

def redact_value(key: str, value: str) -> str:
    key_lower = key.lower()
    stripped = value.strip()

    if key_lower in {"model", "model_reasoning_effort", "approval_policy", "sandbox_mode", "web_search", "personality"}:
        return value

    if key_lower in {"command"}:
        return value

    if key_lower in {"url"}:
        if "project_ref=" in stripped:
            return re.sub(r"project_ref=[^\"&]+", "project_ref=YOUR_PROJECT_REF", value)
        return value

    if key_lower in {"args"}:
        if "/Users/" in stripped or "\\\\" in stripped:
            return '["/path/to/your/local/tool"]'
        return value

    if any(token in key_lower for token in ("key", "token", "secret", "password", "authorization")):
        indent = value[: len(value) - len(value.lstrip())]
        return f'{indent}"YOUR_{key.upper()}_HERE"'

    if key_lower.endswith("_url"):
        indent = value[: len(value) - len(value.lstrip())]
        return f'{indent}"https://your-service.example.com"'

    if key_lower == "enabled":
        return value

    return value

for line in text.splitlines():
    stripped = line.strip()

    if skip_legacy_browser_block:
        if stripped.startswith("[") and not stripped.startswith("[mcp_servers.chrome-devtools"):
            skip_legacy_browser_block = False
        else:
            continue

    if stripped.startswith("[mcp_servers.chrome-devtools"):
        skip_legacy_browser_block = True
        continue

    if stripped.startswith('[projects."'):
        skip_project_block = True
        continue
    if skip_project_block:
        if stripped.startswith("[") and not stripped.startswith('[projects."'):
            skip_project_block = False
        else:
            continue

    if stripped.startswith("[mcp_servers.gemini-design-mcp]"):
        lines.append(line)
        continue

    if stripped.startswith("[notice.model_migrations]"):
        lines.append(line)
        continue

    if "=" in line and not stripped.startswith("#"):
        key, value = line.split("=", 1)
        redacted = redact_value(key.strip(), value)
        lines.append(f"{key}= {redacted.lstrip()}")
    else:
        lines.append(line)

dest.write_text("\n".join(lines).rstrip() + "\n")
PY
  echo "    ✓ config/config.example.toml"
fi

# Sync skills (preserve nested folders like agents/, scripts/, references/, assets/)
if [[ -d "$CODEX_DIR/skills" ]]; then
  mkdir -p "$SCRIPT_DIR/skills"
  for skill_dir in "$CODEX_DIR/skills"/*/; do
    if [[ -d "$skill_dir" ]]; then
      skill_name=$(basename "$skill_dir")
      skill_src="${skill_dir%/}"
      skill_dest="$SCRIPT_DIR/skills/$skill_name"
      mkdir -p "$skill_dest"
      rsync -a --delete \
        --exclude '.DS_Store' \
        "$skill_src/" "$skill_dest/"
      echo "    ✓ skills/$skill_name/"
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
echo "Reminder: Review config/config.example.toml and make sure it contains placeholders only."
