#!/usr/bin/env python3
"""Exercise instruction installation and profile edits in disposable projects."""
from pathlib import Path
import importlib.util
import os
import stat
import shutil
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location('apply_profile', ROOT / 'scripts/apply-profile.py')
profile = importlib.util.module_from_spec(spec)
spec.loader.exec_module(profile)
copy_spec = importlib.util.spec_from_file_location('copy_resources', ROOT / 'scripts/copy-resources.py')
resources = importlib.util.module_from_spec(copy_spec)
copy_spec.loader.exec_module(resources)

class InstructionToolsTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix='instruction-tools-')
        self.root = Path(self.temp.name)
        self.project = self.root / 'project'
        self.project.mkdir()
    def tearDown(self):
        self.temp.cleanup()
    def apply(self, check=False):
        return profile.apply_profile('expo', self.project, ROOT / 'profiles', check)
    def test_preview_does_not_write(self):
        self.apply(check=True)
        self.assertFalse((self.project / 'AGENTS.md').exists())
    def test_update_preserves_human_text_and_is_idempotent(self):
        p = self.project / 'AGENTS.md'
        p.write_text('Human preface\n\n<!-- codex-profile:expo:start -->\nold\n<!-- codex-profile:expo:end -->\nHuman ending\n')
        self.apply()
        first = p.read_bytes()
        self.assertTrue(first.startswith(b'Human preface\n\n'))
        self.assertTrue(first.endswith(b'\nHuman ending\n'))
        self.apply()
        self.assertEqual(first, p.read_bytes())
    def test_integrated_project_stays_in_control(self):
        p = self.project / 'AGENTS.md'
        p.write_text('Project rules\n<!-- codex-profile:expo:integrated -->\n')
        first = p.read_bytes()
        self.apply()
        self.assertEqual(first, p.read_bytes())
    def test_malformed_markers_and_size_fail_without_write(self):
        p = self.project / 'AGENTS.md'
        for text in ['<!-- codex-profile:expo:start -->\n', '<!-- codex-profile:expo:end --><!-- codex-profile:expo:start -->', 'x' * 30000]:
            p.write_text(text)
            with self.assertRaises(ValueError):
                self.apply()
            self.assertEqual(text, p.read_text())
    def test_backslash_text_is_literal(self):
        profiles = self.root / 'profiles/expo'
        profiles.mkdir(parents=True)
        (profiles / 'AGENTS.md').write_text('Regex: \\d+ and \\1 are literal examples.')
        p = self.project / 'AGENTS.md'
        p.write_text('<!-- codex-profile:expo:start -->old<!-- codex-profile:expo:end -->')
        profile.apply_profile('expo', self.project, self.root / 'profiles')
        self.assertIn('\\d+ and \\1', p.read_text())
    def test_crossed_or_nested_profiles_preserve_original(self):
        p = self.project / 'AGENTS.md'
        for text in [
            '<!-- codex-profile:expo:start --><!-- codex-profile:next:start --><!-- codex-profile:expo:end --><!-- codex-profile:next:end -->',
            '<!-- codex-profile:expo:start --><!-- codex-profile:next:start --><!-- codex-profile:next:end --><!-- codex-profile:expo:end -->',
        ]:
            p.write_text(text)
            with self.assertRaises(ValueError):
                self.apply()
            self.assertEqual(text, p.read_text())
    def test_profile_refuses_symbolic_link(self):
        outside = self.root / 'outside.md'
        outside.write_text('outside content')
        (self.project / 'AGENTS.md').symlink_to(outside)
        with self.assertRaises(ValueError):
            self.apply()
        self.assertEqual(outside.read_text(), 'outside content')
    def installer(self, source=None):
        return subprocess.run(['bash', str((source or ROOT) / 'install.sh'), '--project', '--profile', 'expo', '--target', str(self.project), '--yes'], capture_output=True, text=True)
    def sync_fixture(self, target, manifest='fixture\n'):
        (target / 'config').mkdir(parents=True, exist_ok=True)
        (target / 'scripts').mkdir(exist_ok=True)
        shutil.copy2(ROOT / 'sync.sh', target / 'sync.sh')
        shutil.copy2(ROOT / 'scripts/copy-resources.py', target / 'scripts/copy-resources.py')
        (target / 'config/skills-manifest.txt').write_text(manifest)
    def small_installer(self):
        source = self.root / 'installer'
        for name in ['config', 'profiles']:
            shutil.copytree(ROOT / name, source / name)
        (source / 'scripts').mkdir()
        for name in resources.HELPERS:
            shutil.copy2(ROOT / 'scripts' / name, source / 'scripts' / name)
        shutil.copy2(ROOT / 'install.sh', source / 'install.sh')
        (source / 'config/skills-manifest.txt').write_text('fixture\n')
        (source / 'skills/fixture').mkdir(parents=True)
        (source / 'skills/fixture/SKILL.md').write_text('Fixture instructions\n')
        return source
    def synchronize(self, source, target):
        return subprocess.run(['bash', str(target / 'sync.sh'), '--source', str(source)], capture_output=True, text=True)
    def state(self, root):
        result = {}
        for folder, dirs, files in os.walk(root, followlinks=False):
            for name in dirs + files:
                path = Path(folder) / name
                relative = str(path.relative_to(root))
                if path.is_symlink():
                    result[relative] = ('link', os.readlink(path))
                elif path.is_file():
                    result[relative] = ('file', path.read_bytes(), stat.S_IMODE(path.stat().st_mode))
                else:
                    result[relative] = ('dir', stat.S_IMODE(path.stat().st_mode))
        return result
    def test_invalid_manifest_fails_before_any_target_write(self):
        source = self.small_installer()
        (source / 'config/skills-manifest.txt').write_text('missing\n')
        (self.project / 'AGENTS.md').write_text('preserve me')
        result = self.installer(source)
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual((self.project / 'AGENTS.md').read_text(), 'preserve me')
        self.assertFalse((self.project / '.codex').exists())
    def test_install_refuses_linked_skill_before_any_target_write(self):
        outside = self.root / 'outside'
        outside.mkdir()
        (outside / 'SKILL.md').write_text('preserve me')
        skills = self.project / '.codex/skills'
        skills.mkdir(parents=True)
        (skills / 'refresh-context').symlink_to(outside, target_is_directory=True)
        (self.project / 'AGENTS.md').write_text('human rules')
        result = self.installer()
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual((outside / 'SKILL.md').read_text(), 'preserve me')
        self.assertEqual((self.project / 'AGENTS.md').read_text(), 'human rules')
        self.assertFalse((self.project / '.codex/scripts').exists())
    def test_manifest_normalization_matches_preflight_and_install(self):
        source = self.root / 'installer'
        for name in ['config', 'profiles', 'scripts']:
            shutil.copytree(ROOT / name, source / name)
        shutil.copytree(ROOT / 'skills/refresh-context', source / 'skills/refresh-context')
        shutil.copy2(ROOT / 'install.sh', source / 'install.sh')
        (source / 'config/skills-manifest.txt').write_bytes(b'  # comment\r\n  refresh-context  \r\n\t\r\n')
        result = self.installer(source)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue((self.project / '.codex/skills/refresh-context/SKILL.md').is_file())
        self.assertEqual((self.project / '.codex/skills-manifest.txt').read_text(), 'refresh-context\n')
    def test_sync_refuses_linked_destination_before_copy(self):
        source, target, outside = [self.root / name for name in ['source', 'target', 'outside']]
        for path in [source / 'skills/fixture', target / 'skills', outside]:
            path.mkdir(parents=True)
        (source / 'skills-manifest.txt').write_text('fixture\n')
        (source / 'skills/fixture/SKILL.md').write_text('new skill')
        (source / 'AGENTS.md').write_text('new rules')
        (outside / 'SKILL.md').write_text('outside original')
        (target / 'skills/fixture').symlink_to(outside, target_is_directory=True)
        self.sync_fixture(target)
        result = subprocess.run(['bash', str(target / 'sync.sh'), '--source', str(source)], capture_output=True)
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual((outside / 'SKILL.md').read_text(), 'outside original')
        self.assertFalse((target / 'config/AGENTS.md').exists())
    def test_install_then_sync_preserves_full_resources_and_private_config(self):
        codex = self.project / '.codex'
        (codex / 'skills/unrelated').mkdir(parents=True)
        (codex / 'skills/unrelated/keep.txt').write_text('unrelated work')
        private = 'model = "fixture-model"\n[fixture]\nsecret = "TEST_ONLY_SENTINEL"\n'
        (codex / 'config.toml').write_text(private)
        (self.project / 'AGENTS.md').write_text('Human project instructions\n')
        install = subprocess.run(['bash', str(ROOT / 'install.sh'), '--project', '--profile', 'expo', '--target', str(self.project), '--yes'], capture_output=True, text=True)
        self.assertEqual(install.returncode, 0, install.stderr)
        self.assertEqual((codex / 'config.toml').read_text(), private)
        self.assertEqual((codex / 'skills/unrelated/keep.txt').read_text(), 'unrelated work')
        entries = [x.strip() for x in (ROOT / 'config/skills-manifest.txt').read_text().splitlines() if x.strip() and not x.startswith('#')]
        for name in entries:
            for p in (ROOT / 'skills' / name).rglob('*'):
                if p.is_file() and not resources.excluded(p.relative_to(ROOT / 'skills' / name)):
                    dest = codex / 'skills' / name / p.relative_to(ROOT / 'skills' / name)
                    self.assertEqual(p.read_bytes(), dest.read_bytes(), str(dest))
        target = self.root / 'sync-target'
        (target / 'config').mkdir(parents=True)
        self.sync_fixture(target, '\n'.join(entries) + '\n')
        (target / 'config/config.example.toml').write_text('public template only')
        (target / 'unrelated.txt').write_text('keep')
        sync = subprocess.run(['bash', str(target / 'sync.sh'), '--source', str(codex)], capture_output=True, text=True)
        self.assertEqual(sync.returncode, 0, sync.stderr)
        self.assertEqual((target / 'config/config.example.toml').read_text(), 'public template only')
        self.assertEqual((target / 'unrelated.txt').read_text(), 'keep')
        self.assertFalse((target / 'config.toml').exists())
        for name in entries:
            for p in (codex / 'skills' / name).rglob('*'):
                if p.is_file() and not resources.excluded(p.relative_to(codex / 'skills' / name)):
                    self.assertEqual(p.read_bytes(), (target / 'skills' / name / p.relative_to(codex / 'skills' / name)).read_bytes())
    def test_sync_missing_entry_fails_before_copy(self):
        source = self.root / 'source'
        source.mkdir()
        (source / 'skills-manifest.txt').write_text('missing-skill\n')
        (source / 'AGENTS.md').write_text('must not copy')
        target = self.root / 'target'
        target.mkdir()
        self.sync_fixture(target, 'missing-skill\n')
        result = subprocess.run(['bash', str(target / 'sync.sh'), '--source', str(source)], capture_output=True)
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse((target / 'config/AGENTS.md').exists())

    def test_internal_links_metadata_permissions_and_two_install_sync_roundtrips(self):
        source = self.small_installer()
        skill = source / 'skills/fixture'
        (skill / 'AGENTS.md').symlink_to('SKILL.md')
        (skill / 'CLAUDE.md').symlink_to('AGENTS.md')
        (skill / 'references').mkdir()
        (skill / 'references/details.md').write_bytes(b'Reference\x00bytes\n')
        (skill / 'reference-alias').symlink_to('references', target_is_directory=True)
        (skill / 'run.sh').write_text('#!/bin/sh\nexit 0\n')
        (skill / 'run.sh').chmod(0o751)
        (skill / '.git').mkdir()
        (skill / '.git/config').write_text('PRIVATE_GIT_SENTINEL')
        (skill / 'references/.git').write_text('gitdir: PRIVATE_GIT_SENTINEL')
        (skill / '__pycache__').mkdir()
        (skill / '__pycache__/ignored.pyc').write_bytes(b'cache')
        (skill / '.DS_Store').write_bytes(b'metadata')
        (skill / 'node_modules').mkdir()
        (skill / 'node_modules/cache').write_text('ignored')
        codex = self.project / '.codex'
        (self.project / 'AGENTS.md').write_text('Human project rules\n')
        for iteration in range(2):
            result = self.installer(source)
            self.assertEqual(result.returncode, 0, result.stderr)
            installed = codex / 'skills/fixture'
            for name in ['AGENTS.md', 'CLAUDE.md']:
                self.assertFalse((installed / name).is_symlink())
                self.assertEqual((installed / name).read_bytes(), (skill / 'SKILL.md').read_bytes())
            self.assertFalse((installed / 'reference-alias').is_symlink())
            self.assertEqual((installed / 'reference-alias/details.md').read_bytes(), b'Reference\x00bytes\n')
            for name in ['.git', 'references/.git', 'reference-alias/.git', '__pycache__', '.DS_Store', 'node_modules']:
                self.assertFalse((installed / name).exists(), name)
            self.assertEqual(stat.S_IMODE((installed / 'run.sh').stat().st_mode), 0o751)
            self.assertEqual((codex / 'scripts/copy-resources.py').read_bytes(), (ROOT / 'scripts/copy-resources.py').read_bytes())
            current = self.state(codex)
            if iteration == 0:
                first_install = current
            else:
                self.assertEqual(current, first_install)
        self.assertEqual(len(list(self.project.glob('.codex-backup-*'))), 2)
        target = self.root / 'sync-target'
        self.sync_fixture(target)
        # Exercise source symlinks directly in sync, not only the materialized install.
        for name in ['AGENTS.md', 'CLAUDE.md']:
            (codex / 'skills/fixture' / name).unlink()
            (codex / 'skills/fixture' / name).symlink_to('SKILL.md')
        (codex / 'skills/fixture/.git').write_text('gitdir: never-export')
        for iteration in range(2):
            result = self.synchronize(codex, target)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertFalse((target / 'skills/fixture/.git').exists())
            self.assertFalse((target / 'skills/fixture/AGENTS.md').is_symlink())
            self.assertEqual(stat.S_IMODE((target / 'skills/fixture/run.sh').stat().st_mode), 0o751)
            self.assertEqual((target / 'scripts/copy-resources.py').read_bytes(), (ROOT / 'scripts/copy-resources.py').read_bytes())
            current = self.state(target)
            if iteration == 0:
                first_sync = current
            else:
                self.assertEqual(current, first_sync)

    def test_source_escape_cycles_and_excluded_alias_fail_before_any_mutation(self):
        source = self.small_installer()
        skill = source / 'skills/fixture'
        private = source / 'skills/private'
        private.mkdir()
        (private / 'secret.txt').write_text('PRIVATE_SOURCE_SENTINEL')
        target = self.root / 'sync-target'
        self.sync_fixture(target)
        (source / 'AGENTS.md').write_text('rules must not copy on failure')
        (self.project / 'AGENTS.md').write_text('human rules')
        for kind in ['external', 'private-sibling', 'file-cycle', 'directory-cycle', 'dangling', 'excluded-alias']:
            with self.subTest(kind=kind):
                link = skill / 'bad'
                if kind == 'external':
                    outside = self.root / 'outside.txt'
                    outside.write_text('OUTSIDE_SENTINEL')
                    link.symlink_to(outside)
                elif kind == 'private-sibling':
                    link.symlink_to('../private/secret.txt')
                elif kind == 'file-cycle':
                    link.symlink_to('other')
                    (skill / 'other').symlink_to('bad')
                elif kind == 'directory-cycle':
                    link.symlink_to('.', target_is_directory=True)
                elif kind == 'dangling':
                    link.symlink_to('missing')
                else:
                    (skill / '.git').mkdir()
                    (skill / '.git/config').write_text('EXCLUDED_SENTINEL')
                    link.symlink_to('.git/config')
                before_project, before_target = self.state(self.project), self.state(target)
                result = self.installer(source)
                self.assertNotEqual(result.returncode, 0, kind)
                self.assertEqual(self.state(self.project), before_project)
                result = self.synchronize(source, target)
                self.assertNotEqual(result.returncode, 0, kind)
                self.assertEqual(self.state(target), before_target)
                link.unlink()
                if (skill / 'other').is_symlink():
                    (skill / 'other').unlink()
                if (skill / '.git').exists():
                    shutil.rmtree(skill / '.git')

    def test_sync_requires_target_allowlist_and_never_exports_private_source_skills(self):
        source = self.small_installer()
        (source / 'skills-manifest.txt').write_text('fixture\nprivate\n')
        (source / 'skills/private').mkdir()
        (source / 'skills/private/SKILL.md').write_text('PRIVATE_SKILL_SENTINEL')
        (source / 'AGENTS.md').write_text('new rules')
        target = self.root / 'sync-target'
        self.sync_fixture(target, '# Public repository allowlist\nfixture\n')
        (target / 'skills/local-overlay').mkdir(parents=True)
        (target / 'skills/local-overlay/keep').write_text('existing overlay')
        (target / 'config/config.example.toml').write_text('public template')
        allowlist = (target / 'config/skills-manifest.txt').read_bytes()
        before_source = self.state(source)
        result = self.synchronize(source, target)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual((target / 'config/skills-manifest.txt').read_bytes(), allowlist)
        self.assertFalse((target / 'skills/private').exists())
        self.assertEqual((target / 'skills/local-overlay/keep').read_text(), 'existing overlay')
        self.assertEqual((target / 'config/config.example.toml').read_text(), 'public template')
        self.assertEqual(self.state(source), before_source)
        (target / 'config/skills-manifest.txt').unlink()
        before_target = self.state(target)
        result = self.synchronize(source, target)
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(self.state(target), before_target)

    def test_runtime_data_stays_local_while_reference_data_and_templates_copy(self):
        source = self.small_installer()
        skill = source / 'skills/fixture'
        private_paths = ['company.json', 'copros.json', 'data/journal-entries.json',
                         'data/invoices/index.json', 'data/invoices/invoice-001.json',
                         'data/invoices/2026/invoice.pdf', '.env', '.env.local', 'auth.json',
                         'config.toml', 'data/transactions/private.json',
                         'data/imports/bank.csv', 'output/report.pdf', 'copros/private.json']
        public_paths = ['company.example.json', 'data/invoices/_template.json',
                        'data/pcg-reference.json', 'evals/files/company.json',
                        'evals/files/data/journal-entries.json', 'templates/report.html',
                        'evals/files/data/transactions/sample.json']
        for name in private_paths + public_paths:
            path = skill / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text('PRIVATE_RUNTIME_SENTINEL' if name in private_paths else 'REFERENCE_SENTINEL')
        codex = self.project / '.codex'
        local_journal = codex / 'skills/fixture/data/journal-entries.json'
        local_journal.parent.mkdir(parents=True)
        local_journal.write_text('EXISTING_LOCAL_JOURNAL')
        result = self.installer(source)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(local_journal.read_text(), 'EXISTING_LOCAL_JOURNAL')
        for name in private_paths:
            if name != 'data/journal-entries.json':
                self.assertFalse((codex / 'skills/fixture' / name).exists(), name)
        for name in public_paths:
            self.assertEqual((codex / 'skills/fixture' / name).read_text(), 'REFERENCE_SENTINEL')
        target = self.root / 'sync-target'
        self.sync_fixture(target)
        existing_invoice = target / 'skills/fixture/data/invoices/index.json'
        existing_invoice.parent.mkdir(parents=True)
        existing_invoice.write_text('EXISTING_TARGET_INVOICE')
        # Sync the original source containing every private sentinel.
        result = self.synchronize(source, target)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(existing_invoice.read_text(), 'EXISTING_TARGET_INVOICE')
        for name in private_paths:
            if name != 'data/invoices/index.json':
                self.assertFalse((target / 'skills/fixture' / name).exists(), name)
        for name in public_paths:
            self.assertEqual((target / 'skills/fixture' / name).read_text(), 'REFERENCE_SENTINEL')

    def test_global_instruction_link_cannot_export_private_config(self):
        source = self.small_installer()
        (source / 'config.toml').write_text('PRIVATE_CONFIG_SENTINEL')
        (source / 'AGENTS.md').symlink_to('config.toml')
        target = self.root / 'sync-target'
        self.sync_fixture(target)
        before = self.state(target)
        result = self.synchronize(source, target)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('Global instruction source must be a regular file', result.stderr)
        self.assertEqual(self.state(target), before)

    def test_existing_internal_destination_links_require_explicit_migration(self):
        source = self.small_installer()
        installed = self.project / '.codex/skills/fixture'
        installed.mkdir(parents=True)
        (installed / 'SKILL.md').write_text('existing local skill')
        (installed / 'AGENTS.md').symlink_to('SKILL.md')
        before = self.state(self.project)
        result = self.installer(source)
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(self.state(self.project), before)
        self.assertIn('Symbolic-link destination', result.stderr)
        target = self.root / 'sync-target'
        self.sync_fixture(target)
        (target / 'skills/fixture').mkdir(parents=True)
        (target / 'skills/fixture/SKILL.md').write_text('existing repository skill')
        (target / 'skills/fixture/AGENTS.md').symlink_to('SKILL.md')
        before = self.state(target)
        result = self.synchronize(source, target)
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(self.state(target), before)

    def test_destination_type_conflict_fails_before_any_copy(self):
        source = self.small_installer()
        installed = self.project / '.codex/skills/fixture/SKILL.md'
        installed.mkdir(parents=True)
        (self.project / 'AGENTS.md').write_text('human rules')
        before = self.state(self.project)
        result = self.installer(source)
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(self.state(self.project), before)
        target = self.root / 'sync-target'
        self.sync_fixture(target)
        (target / 'skills/fixture/SKILL.md').mkdir(parents=True)
        before = self.state(target)
        result = self.synchronize(source, target)
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(self.state(target), before)

if __name__ == '__main__':
    unittest.main(verbosity=2)
