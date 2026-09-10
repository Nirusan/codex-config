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
    parser.add_argument("--check", action="store_true", help="Preview without writing")
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


def apply_profile(profile: str, target_dir: Path, profiles_dir: Path, check: bool = False) -> tuple[Path, str]:
    if not target_dir.is_dir():
        raise NotADirectoryError(f"Target directory does not exist: {target_dir}")

    profile_text = read_profile(profile, profiles_dir)
    agents_path = target_dir / "AGENTS.md"
    if agents_path.is_symlink():
        raise ValueError("AGENTS.md is a symbolic link; no target file changed")
    start_marker = f"<!-- codex-profile:{profile}:start -->"
    end_marker = f"<!-- codex-profile:{profile}:end -->"
    block = f"{start_marker}\n{profile_text}\n{end_marker}"

    if agents_path.exists():
        current = agents_path.read_text(encoding="utf-8")
    else:
        current = "# Project Codex Instructions\n"

    opened = None
    seen = set()
    for match in re.finditer(r"<!-- codex-profile:(next|expo):(start|end) -->", current):
        name, kind = match.groups()
        if kind == "start":
            if opened is not None or name in seen:
                raise ValueError("Nested or duplicate profile blocks; no file changed")
            opened = name
            seen.add(name)
        elif opened != name:
            raise ValueError("Crossed or unmatched profile markers; no file changed")
        else:
            opened = None
    if opened is not None:
        raise ValueError("Unclosed profile marker; no file changed")
    if f"<!-- codex-profile:{profile}:integrated -->" in current:
        return agents_path, "already integrated; project maintains its own guidance"
    if current.count(start_marker) != current.count(end_marker) or current.count(start_marker) > 1:
        raise ValueError("Malformed or duplicate profile markers; preserve and repair them before applying")
    if start_marker in current and current.index(end_marker) < current.index(start_marker):
        raise ValueError("Reversed profile markers; no file changed")

    pattern = re.compile(
        rf"{re.escape(start_marker)}.*?{re.escape(end_marker)}",
        flags=re.DOTALL,
    )

    if pattern.search(current):
        updated = pattern.sub(lambda _: block, current)
        action = "updated"
    else:
        separator = "\n\n" if current.strip() else ""
        updated = f"{current.rstrip()}{separator}{block}\n"
        action = "added"

    if len(updated.encode("utf-8")) > 30000:
        raise ValueError("AGENTS would exceed the 30 KB instruction budget; move task-specific detail to references first")
    if updated == current:
        return agents_path, "unchanged"
    if check:
        return agents_path, f"would be {action} ({len(updated.encode('utf-8'))} bytes)"
    if updated != current:
        agents_path.write_text(updated, encoding="utf-8")

    return agents_path, action


def main() -> int:
    args = parse_args()
    target_dir = Path(args.target).expanduser().resolve()
    profiles_dir = resolve_profiles_dir(args.profiles_dir)

    try:
        agents_path, action = apply_profile(args.profile, target_dir, profiles_dir, args.check)
    except (FileNotFoundError, NotADirectoryError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    print(f"{action} codex-profile:{args.profile} in {agents_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
