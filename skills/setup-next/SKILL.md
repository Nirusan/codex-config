---
name: setup-next
description: Set up or refresh project instructions for an explicitly requested Next configuration audit.
---

# Setup Next

Resolve the requested target and inspect its instructions, package manifest and Next/React dependencies, App Router or Pages Router, Next config, styling and validation scripts before editing. This skill configures instructions; it does not authorize application changes or dependency installation.

If the project already integrates equivalent maintained guidance (including `codex-profile:next:integrated`), reconcile only an actual gap instead of appending a second profile. Otherwise use the installed `scripts/apply-profile.py --profile next --target <path> --check` to preview, then apply the same command without `--check` within the requested setup scope. The helper is at `${CODEX_HOME:-$HOME/.codex}/scripts/apply-profile.py`, or in the configuration repository.

Preserve project instructions outside the managed block. A stack mismatch must be reported; apply an unmatched profile only if the user explicitly requested that choice. Report detected versions, the actual instruction change and relevant missing checks. Do not output a second catalogue of companion skills or run every diagnostic by default.
