#!/usr/bin/env python3
"""Preflight and copy public instruction resources without links or runtime data.

Each skill/profile is its own source boundary. Snapshots contain bytes and modes,
so validation finishes before destination writes and copying never follows source
links again. This is preflight safety, not a transaction against concurrent edits.
"""
from pathlib import Path
from typing import NamedTuple, Optional
import os
import stat
import sys


INCIDENTAL = {'.git', '.DS_Store', '__pycache__', 'node_modules', '.cache',
              '.pytest_cache', '.mypy_cache', '.ruff_cache', '.pnpm-store',
              '.venv', 'venv', '.tox', 'Thumbs.db', 'desktop.ini'}
HELPERS = ('apply-profile.py', 'copy-resources.py')


def excluded(relative):
    """Keep reference/example data; exclude metadata and personal runtime files."""
    parts = relative.parts
    if any(p in INCIDENTAL or p.endswith(('.pyc', '.pyo')) for p in parts):
        return True
    if any(p == '.env' or p.startswith('.env.') or p in {'auth.json', 'config.toml'} for p in parts):
        return True
    # These are runtime paths relative to a skill, not similarly named eval fixtures.
    if relative.as_posix() in {'company.json', 'copros.json', 'data/journal-entries.json'}:
        return True
    if parts[:1] in {('output',), ('copros',)} or parts[:2] in {('data', 'transactions'), ('data', 'imports')}:
        return True
    if parts[:2] == ('data', 'invoices') and len(parts) > 2:
        return relative.as_posix() != 'data/invoices/_template.json'
    return False


def inside(path, root):
    try:
        path.relative_to(root)
        return True
    except ValueError:
        return False


def resolve_inside(path, root, links=()):
    """Resolve every link hop within root, including intermediate directories."""
    path = Path(os.path.abspath(path))
    if not inside(path, root):
        raise ValueError(f'Source link escapes its resource directory: {path}')
    cursor = root
    parts = path.relative_to(root).parts
    for index, name in enumerate(parts):
        cursor = cursor / name
        info = cursor.lstat()
        if stat.S_ISLNK(info.st_mode):
            if cursor in links:
                raise ValueError(f'Cyclic source link: {cursor}')
            target = Path(os.readlink(cursor))
            target = Path(os.path.abspath(target if target.is_absolute() else cursor.parent / target))
            if not inside(target, root):
                raise ValueError(f'Source link escapes its resource directory: {cursor}')
            resolved = resolve_inside(target, root, links + (cursor,))
            return resolve_inside(resolved.joinpath(*parts[index + 1:]), root, links + (cursor,))
    if excluded(path.relative_to(root)):
        raise ValueError(f'Source link targets excluded metadata or runtime data: {path}')
    return cursor


class Node(NamedTuple):
    data: Optional[bytes]
    mode: int
    mtime_ns: int


def resource_root(base, relative):
    root = base / relative
    cursor = root
    while cursor != base:
        if cursor.is_symlink():
            raise ValueError(f'Source resource boundary cannot be a link: {cursor}')
        cursor = cursor.parent
    if not root.is_dir():
        raise ValueError(f'Missing source directory: {root}')
    return root


def snapshot(root, relative=Path('.')):
    nodes = {}

    def visit(path, output, ancestors):
        if excluded(output):
            return
        resolved = resolve_inside(path, root)
        info = resolved.stat()
        mode = stat.S_IMODE(info.st_mode)
        if stat.S_ISDIR(info.st_mode):
            if resolved in ancestors:
                raise ValueError(f'Cyclic source directory link: {path}')
            nodes[output] = Node(None, mode, info.st_mtime_ns)
            for child in sorted(resolved.iterdir()):
                visit(child, output / child.name, ancestors + (resolved,))
        elif stat.S_ISREG(info.st_mode):
            nodes[output] = Node(resolved.read_bytes(), mode, info.st_mtime_ns)
        else:
            raise ValueError(f'Unsupported source resource type: {path}')

    visit(root / relative, relative, ())
    return nodes


def snapshot_file(root, relative):
    nodes = snapshot(root, relative)
    if relative not in nodes or nodes[relative].data is None:
        raise ValueError(f'Missing regular source file: {root / relative}')
    return nodes


def reject_destination_links(path, boundary):
    cursor = path
    while True:
        if cursor.is_symlink():
            raise ValueError(f'Symbolic-link destination: {cursor}')
        if cursor == boundary or cursor.parent == cursor:
            break
        if cursor.exists() and cursor != path and not cursor.is_dir():
            raise ValueError(f'Non-directory destination ancestor: {cursor}')
        cursor = cursor.parent
    if path.is_dir():
        for folder, dirs, files in os.walk(path, followlinks=False):
            for name in dirs + files:
                if (Path(folder) / name).is_symlink():
                    raise ValueError(f'Symbolic-link destination under {path}')


def validate_plan(nodes, managed, boundary):
    for path in managed:
        reject_destination_links(path, boundary)
    for path, node in nodes.items():
        reject_destination_links(path, boundary)
        if path.exists():
            if node.data is None and not path.is_dir():
                raise ValueError(f'Destination must be a directory: {path}')
            if node.data is not None and not path.is_file():
                raise ValueError(f'Destination must be a regular file: {path}')


def write_plan(nodes):
    new_dirs = []
    for path, node in sorted(nodes.items(), key=lambda item: len(item[0].parts)):
        if node.data is None:
            if not path.exists():
                path.mkdir(parents=True)
                new_dirs.append((path, node))
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            # Replace regular files instead of altering any hard-linked sibling.
            if path.exists():
                path.unlink()
            path.write_bytes(node.data)
            path.chmod(node.mode)
            os.utime(path, ns=(node.mtime_ns, node.mtime_ns))
    for path, node in reversed(new_dirs):
        path.chmod(node.mode)
        os.utime(path, ns=(node.mtime_ns, node.mtime_ns))


def entries_from(data):
    entries = [line.strip() for line in data.decode('utf-8').splitlines()
               if line.strip() and not line.lstrip().startswith('#')]
    seen = []
    for name in entries:
        relative = Path(name)
        if relative.is_absolute() or any(p in {'', '.', '..'} for p in name.split('/')):
            raise ValueError(f'Invalid manifest entry: {name}')
        if excluded(relative):
            raise ValueError(f'Manifest entry names excluded resources: {name}')
        if any(relative == other or inside(relative, other) or inside(other, relative) for other in seen):
            raise ValueError(f'Duplicate or overlapping manifest entry: {name}')
        seen.append(relative)
    return entries


def add(nodes, dest, source_nodes):
    for relative, node in source_nodes.items():
        nodes[dest / relative] = node


def skill_snapshot(source, name):
    root = resource_root(source, Path('skills') / name)
    nodes = snapshot(root)
    if Path('SKILL.md') not in nodes or nodes[Path('SKILL.md')].data is None:
        raise ValueError(f'Missing source skill: {name}')
    return nodes


def prepare_install(source, codex, agents, stage):
    config = resource_root(source, Path('config'))
    manifest_node = snapshot_file(config, Path('skills-manifest.txt'))[Path('skills-manifest.txt')]
    entries = entries_from(manifest_node.data)
    staged = {}
    for name in ('AGENTS.md', 'config.example.toml'):
        add(staged, stage / 'config', snapshot_file(config, Path(name)))
    for name in HELPERS:
        add(staged, stage / 'scripts', snapshot_file(resource_root(source, Path('scripts')), Path(name)))
    for name in ('next', 'expo'):
        nodes = snapshot(resource_root(source, Path('profiles') / name))
        if Path('AGENTS.md') not in nodes or nodes[Path('AGENTS.md')].data is None:
            raise ValueError(f'Missing profile entrypoint: {name}')
        add(staged, stage / 'profiles' / name, nodes)
    for name in entries:
        add(staged, stage / 'skills' / name, skill_snapshot(source, name))
    staged[stage / 'config/skills-manifest.txt'] = Node(('\n'.join(entries) + '\n').encode(), 0o644, manifest_node.mtime_ns)
    target_nodes = {}
    for path, node in staged.items():
        relative = path.relative_to(stage)
        if relative == Path('config/AGENTS.md'):
            dest = agents
        elif relative == Path('config/config.example.toml'):
            dest = codex / 'config.toml'
        elif relative == Path('config/skills-manifest.txt'):
            dest = codex / 'skills-manifest.txt'
        else:
            dest = codex / relative
        target_nodes[dest] = node
    managed = [agents, codex / 'config.toml', codex / 'profiles', codex / 'scripts', codex / 'skills-manifest.txt']
    managed += [codex / 'skills' / name for name in entries]
    validate_plan(target_nodes, managed, codex.parent)
    write_plan(staged)


def sync(source, target):
    # The public repository's allowlist is authoritative. Never import a personal manifest.
    manifest = target / 'config/skills-manifest.txt'
    reject_destination_links(manifest, target)
    entries = entries_from(manifest.read_bytes())
    nodes = {}
    managed = [manifest, target / 'config/AGENTS.md']
    for relative in [Path('AGENTS.md')] + [Path('scripts') / name for name in HELPERS]:
        path = source / relative
        if os.path.lexists(path):
            if relative == Path('AGENTS.md') and path.is_symlink():
                raise ValueError(f'Global instruction source must be a regular file, not a link: {path}')
            root = source if relative == Path('AGENTS.md') else resource_root(source, Path('scripts'))
            src = Path('AGENTS.md') if relative == Path('AGENTS.md') else Path(relative.name)
            dest = target / 'config' if relative == Path('AGENTS.md') else target / 'scripts'
            add(nodes, dest, snapshot_file(root, src))
        managed.append(target / ('config/AGENTS.md' if relative == Path('AGENTS.md') else relative))
    for name in entries:
        dest = target / 'skills' / name
        add(nodes, dest, skill_snapshot(source, name))
        managed.append(dest)
    for name in ('next', 'expo'):
        if os.path.lexists(source / 'profiles' / name):
            dest = target / 'profiles' / name
            add(nodes, dest, snapshot(resource_root(source, Path('profiles') / name)))
            managed.append(dest)
    validate_plan(nodes, managed, target)
    write_plan(nodes)
    print(f'Synced instructions and {len(entries)} allowlisted skill directories for review.')
    print('Repository allowlist, template, private config and unlisted resources preserved.')
    print('No staging, commit or push performed. Review exact paths before publication.')


def main():
    if len(sys.argv) == 6 and sys.argv[1] == 'prepare-install':
        source = Path(sys.argv[2]).resolve(strict=True)
        prepare_install(source, *(Path(os.path.abspath(p)) for p in sys.argv[3:]))
    elif len(sys.argv) == 4 and sys.argv[1] == 'sync':
        sync(Path(sys.argv[2]).resolve(strict=True), Path(sys.argv[3]).resolve(strict=True))
    else:
        raise ValueError('Usage: copy-resources.py prepare-install SOURCE CODEX AGENTS STAGE | sync SOURCE TARGET')


if __name__ == '__main__':
    try:
        main()
    except (OSError, ValueError, UnicodeError) as error:
        raise SystemExit(f'error: {error}; copy aborted')
