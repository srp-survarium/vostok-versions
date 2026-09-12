import contextlib
import hashlib
import io
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import source_files_report as report  # noqa: E402


def checksum(digit, algorithm='md5'):
    return {'algorithm': algorithm, 'digest': digit * report.ALGORITHMS[algorithm]}


class SourceFileTests(unittest.TestCase):
    def test_headers_and_windows_case_are_included_and_deduplicated(self):
        records = report.parse_checksums('md5\t' + 'a' * 32 + '\tVostok\\Game\\a.h\n'
                                         'md5\t' + 'a' * 32 + '\tvostok/game/a.h\n')
        self.assertEqual(list(records), ['vostok/game/a.h'])
        self.assertEqual(report.file_kind('vostok/game/a.h'), 'header')

    def test_conflicting_hashes_are_not_silently_overwritten(self):
        with self.assertRaisesRegex(ValueError, 'conflicting'):
            report.parse_checksums('md5\t' + 'a' * 32 + '\ta.cpp\n'
                                   'md5\t' + 'b' * 32 + '\ta.cpp\n')

    def test_invalid_tables_and_paths_fail(self):
        for text in ['', 'garbage', 'md5\txyz\ta.cpp', 'md5\t' + 'a' * 32 + '\t../a.cpp',
                     'none\tabc\ta.cpp', 'md5\t' + 'a' * 32 + '\tC:/a.cpp']:
            with self.subTest(text=text), self.assertRaises(ValueError):
                report.parse_checksums(text)

    def test_missing_and_incompatible_checksums_are_unknown(self):
        none = {'algorithm': 'none', 'digest': ''}
        before = {'both.h': none, 'one.h': checksum('a'), 'algorithm.h': checksum('a')}
        after = {'both.h': none, 'one.h': none, 'algorithm.h': checksum('a', 'sha1')}
        rows = report.compare(before, after)
        self.assertEqual(report.counts(rows)['unknown'], 3)
        self.assertEqual(report.counts(rows)['unchanged'], 0)

    def test_changed_unchanged_and_pdb_only_paths(self):
        before = {'vostok/a.cpp': checksum('a'), 'vostok/b.h': checksum('b'),
                  'boost/gone.hpp': checksum('c')}
        after = {'vostok/a.cpp': checksum('b'), 'vostok/b.h': checksum('b'),
                 'boost/new.hpp': checksum('c')}
        rows = report.compare(before, after)
        self.assertEqual(report.counts(rows), {'changed': 1, 'unchanged': 1, 'added': 1,
                                               'removed': 1, 'unknown': 0})
        self.assertEqual(next(r for r in rows if r['path'] == 'boost/new.hpp')['scope'], 'third_party')
        # Equal hashes at different paths must not be silently treated as unchanged.
        self.assertEqual(next(r for r in rows if r['path'] == 'boost/new.hpp')['status'], 'added')

    def test_complete_file_lists_include_both_hashes(self):
        with tempfile.TemporaryDirectory() as temp:
            output = Path(temp)
            rows = report.compare({'vostok/a.cpp': checksum('a')},
                                  {'vostok/a.cpp': checksum('b'), 'vostok/b.h': checksum('c')})
            summary = report.write_pair(output, 'a', 'b', rows)
            pair = output / 'pairs/a__b'
            self.assertEqual((pair / 'changed.txt').read_text(), 'vostok/a.cpp\n')
            self.assertEqual((pair / 'added.txt').read_text(), 'vostok/b.h\n')
            self.assertEqual(summary['engine_source']['changed'], 1)
            self.assertEqual(summary['engine_header']['added'], 1)
            self.assertIn('a' * 32, (pair / 'files.tsv').read_text())
            self.assertIn('b' * 32, (pair / 'files.tsv').read_text())

    def run_fixture(self, root, expected=None, fail_tool=False):
        inputs = {label: root / f'{label}.pdb' for label in ('a', 'b')}
        for label, path in inputs.items():
            path.write_text(label)
        output = root / 'report'
        (root / 'flake.lock').write_text('{}')
        (root / 'flake.nix').write_text('{}')
        (root / 'patches').mkdir(exist_ok=True)
        (root / 'patches/pdb-diff-all-files.patch').write_text('fixture')

        def tool(args, **kwargs):
            if '--help' in args:
                return subprocess.CompletedProcess(args, 0, '--all-files --list-checksums', '')
            if fail_tool:
                raise subprocess.CalledProcessError(1, args)
            digest = 'a' if args[args.index('--target-pdb') + 1].endswith('a.pdb') else 'b'
            return subprocess.CompletedProcess(args, 0, 'md5\t' + digest * 32 + '\tvostok/a.cpp\n', '')

        with patch.object(report.c, 'REPO_DIR', root), \
             patch.object(report.c, 'chain_versions', return_value=[{'label': label, 'engine_path': f'c:/{label}/sources'} for label in inputs]), \
             patch.object(report.c, 'tool_identity', return_value={'path': '/fixture', 'sha256': 'fixture'}), \
             patch.object(report, 'expected_pdb_hash', return_value=expected), \
             patch.object(report.subprocess, 'run', side_effect=tool), \
             patch.object(sys, 'argv', ['report', '--output', str(output), '--pdb', f'a={inputs["a"]}', '--pdb', f'b={inputs["b"]}']), \
             contextlib.redirect_stdout(io.StringIO()):
            report.main()
        return output

    def test_manifest_records_coverage_and_verifiable_artifacts(self):
        with tempfile.TemporaryDirectory() as temp:
            output = self.run_fixture(Path(temp))
            manifest = json.loads((output / 'manifest.json').read_text())
            self.assertTrue(manifest['complete_chain'])
            self.assertEqual(manifest['pairs'][0]['engine']['changed'], 1)
            self.assertFalse((output / 'INCOMPLETE').exists())
            for path, digest in manifest['files'].items():
                self.assertEqual(hashlib.sha256((output / path).read_bytes()).hexdigest(), digest)

    def test_wrong_pdb_identity_fails_before_comparison(self):
        with tempfile.TemporaryDirectory() as temp:
            with self.assertRaisesRegex(SystemExit, 'PDB hash'):
                self.run_fixture(Path(temp), expected='wrong')
            self.assertTrue((Path(temp) / 'report/INCOMPLETE').exists())
            self.assertFalse((Path(temp) / 'report/manifest.json').exists())

    def test_failed_extraction_leaves_incomplete_report(self):
        with tempfile.TemporaryDirectory() as temp:
            with self.assertRaises(subprocess.CalledProcessError):
                self.run_fixture(Path(temp), fail_tool=True)
            self.assertTrue((Path(temp) / 'report/INCOMPLETE').exists())
            self.assertFalse((Path(temp) / 'report/manifest.json').exists())
