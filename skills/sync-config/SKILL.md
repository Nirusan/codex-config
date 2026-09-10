---
name: sync-config
description: Copy personal Codex instructions and complete skill resources into the configuration repository for review.
---

# Sync configuration

Locate the configuration checkout and inspect its status before copying. Preserve unrelated edits and use an owned worktree if this repository requires isolation or the target paths overlap another task. Run its `sync.sh --source <personal-configuration-directory>` when selecting a source explicitly.

Before execution, inspect the selected `sync.sh` and its copy helper: these instructions describe the reviewed version with a destination allowlist and runtime-data exclusions. If it exports private `config.toml` or runtime data, expands scope from the personal manifest, or stages/commits/pushes automatically, do not run it. Use the reviewed updated script from the configuration worktree or perform only the scoped instruction/resource copy directly. A new skill body does not upgrade an older repository script by itself.

The destination repository's `config/skills-manifest.txt` is the publication allowlist. Sync only its listed skills, including invocation policies and distributable resources, plus AGENTS, profiles and instruction helpers. A larger personal manifest must never expand this scope. Private project skills and runtime data remain local; preserve unlisted files. Add a skill to the repository manifest only after reviewing every resource for public distribution. Do not silently reinstate retired entries.

Local `config.toml` is never exported. Keep the public example curated with placeholders; inspect any requested template edit for secrets and personal paths. Do not read or print credential values for an instruction sync.

Review exact changed paths. Sync alone authorizes no staging, commit or push. If publication is explicitly requested, stage only the audited intended paths and use the user's scoped commit/push authority. Never use `git add -A` on a dirty configuration checkout.
