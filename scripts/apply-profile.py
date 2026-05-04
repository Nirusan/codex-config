#!/usr/bin/env python3
"""Apply a Codex project profile to a target AGENTS.md file."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

VALID_PROFILES = {"next", "expo"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Apply a Codex profile block to AGENTS.md")
    parser.add_argument("--profile", required=True, choices=sorted(VALID_PROFILES))
    parser.add_argument("--target", default=".", help="Project directory to update")
    parser.add_argument(
        "--profiles-dir",
        default=None,
        help="Directory containing <profile>/AGENTS.md files",
    )
    return parser.parse_args()


def resolve_profiles_dir(raw_profiles_dir: str | None) -> Path:
    if raw_profiles_dir:
        return Path(raw_profiles_dir).expanduser().resolve()

    script_path = Path(__file__).resolve()
    return script_path.parent.parent / "profiles"


def read_profile(profile: str, profiles_dir: Path) -> str:
    profile_path = profiles_dir / profile / "AGENTS.md"
    if not profile_path.is_file():
        raise FileNotFoundError(f"Profile file not found: {profile_path}")

    return profile_path.read_text(encoding="utf-8").strip()


def apply_profile(profile: str, target_dir: Path, profiles_dir: Path) -> tuple[Path, str]:
    if not target_dir.is_dir():
        raise NotADirectoryError(f"Target directory does not exist: {target_dir}")

    profile_text = read_profile(profile, profiles_dir)
    agents_path = target_dir / "AGENTS.md"
    start_marker = f"<!-- codex-profile:{profile}:start -->"
    end_marker = f"<!-- codex-profile:{profile}:end -->"
    block = f"{start_marker}\n{profile_text}\n{end_marker}"

    if agents_path.exists():
        current = agents_path.read_text(encoding="utf-8")
    else:
        current = "# Project Codex Instructions\n"

    pattern = re.compile(
        rf"{re.escape(start_marker)}.*?{re.escape(end_marker)}",
        flags=re.DOTALL,
    )

    if pattern.search(current):
        updated = pattern.sub(block, current)
        action = "updated"
    else:
        separator = "\n\n" if current.strip() else ""
        updated = f"{current.rstrip()}{separator}{block}\n"
        action = "added"

    if updated != current:
        agents_path.write_text(updated, encoding="utf-8")

    return agents_path, action


def main() -> int:
    args = parse_args()
    target_dir = Path(args.target).expanduser().resolve()
    profiles_dir = resolve_profiles_dir(args.profiles_dir)

    try:
        agents_path, action = apply_profile(args.profile, target_dir, profiles_dir)
    except (FileNotFoundError, NotADirectoryError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    print(f"{action} codex-profile:{args.profile} in {agents_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
