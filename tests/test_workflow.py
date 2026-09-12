import base64
import contextlib
import io
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

SCRIPTS = Path(__file__).resolve().parents[1] / 'scripts'
sys.path.insert(0, str(SCRIPTS))
import add_version as av  # noqa: E402
import chain_report as cr  # noqa: E402
import common as c  # noqa: E402
import deps_report as dr  # noqa: E402
import diff_versions as dv  # noqa: E402
import flags_report as fr  # noqa: E402


class WorkflowTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.catalog = self.root / 'catalog'
        self.catalog.mkdir()
        self.versions = self.root / 'work/versions'
        self.reports = self.root / 'work/reports'
        self.diffs = self.root / 'work/diffs'
        self.entries = [{'label': label, 'build': i} for i, label in enumerate(['a', 'b', 'c'])]
        (self.catalog / 'versions.json').write_text(json.dumps(self.entries))
        (self.catalog / 'chain.json').write_text(json.dumps({'base': 'a', 'versions': ['a', 'b', 'c']}))
        (self.root / 'flake.lock').write_text('{}')
        for name, value in {'REPO_DIR': self.root, 'VERSIONS_DIR': self.versions,
                            'DIFFS_DIR': self.diffs, 'REPORTS_DIR': self.reports,
                            'REGISTRY_PATH': self.catalog / 'versions.json',
                            'CONFIG_PATH': self.catalog / 'chain.json'}.items():
            self.start(patch.object(c, name, value))
        self.start(patch.object(c, 'tool_identity', return_value={'path': '/fixture/tool', 'sha256': 'tool'}))
        self.start(patch.object(c, 'require_tool', side_effect=lambda name: name))
        self.start(patch.object(c, 'delinker_supports', return_value=True))
        self.start(patch.object(cr, 'REPORTS_DIR', self.reports))
        self.start(patch.object(fr, 'REPORTS_DIR', self.reports))
        self.start(patch.object(dr, 'REPORTS_DIR', self.reports))
        self.start(patch.object(dr, 'EXTRA_PATH', self.catalog / 'extra_builds.json'))
        self.source = self.root / 'input'
        self.source.mkdir()
        (self.source / 'survarium.exe').write_bytes(b'exe')
        (self.source / 'survarium.pdb').write_bytes(b'pdb')

    def start(self, patcher):
        value = patcher.start()
        self.addCleanup(patcher.stop)
        return value

    def ingest_fixture(self, label):
        root = self.versions / label
        (root / 'objects/vostok').mkdir(parents=True, exist_ok=True)
        (root / 'objects/vostok/unit.obj').write_bytes(b'obj-' + label.encode())
        (root / 'meta.json').write_text('{}')
        return root

    def fake_delinker(self, args, **kwargs):
        out = Path(args[args.index('--output-path') + 1])
        (out / 'unit.obj').write_bytes(b'object')
        return subprocess.CompletedProcess(args, 0)

    def run_ingest(self, *extra):
        with patch.object(sys, 'argv', ['add_version.py', 'b', str(self.source), '--no-structure', *extra]), contextlib.redirect_stdout(io.StringIO()):
            av.main()
        return json.loads((self.versions / 'b/meta.json').read_text())

    def test_metadata_without_objects_does_not_skip_ingestion(self):
        path = self.versions / 'b'
        path.mkdir(parents=True)
        (path / 'meta.json').write_text('{}')
        with patch.object(av.subprocess, 'run', side_effect=self.fake_delinker) as tool:
            meta = self.run_ingest()
        self.assertEqual(tool.call_count, 1)
        self.assertEqual(meta['n_objects'], 1)

    def test_failed_alignment_records_actual_fallback(self):
        root = self.ingest_fixture('a')
        (root / 'symbol-map.tsv').write_text('base map')
        def run(args, **kwargs):
            if '--read-symbol-map' in args:
                raise subprocess.CalledProcessError(1, args)
            return self.fake_delinker(args)
        with patch.object(av.subprocess, 'run', side_effect=run):
            meta = self.run_ingest('--align-to', 'a')
        self.assertIsNone(meta['aligned_to'])
        self.assertEqual(meta['alignment']['requested'], 'a')
        self.assertEqual(meta['alignment']['status'], 'failed-fallback')

    def test_successful_alignment_records_map_hash(self):
        root = self.ingest_fixture('a')
        (root / 'symbol-map.tsv').write_text('base map')
        with patch.object(av.subprocess, 'run', side_effect=self.fake_delinker):
            meta = self.run_ingest('--align-to', 'a')
        self.assertEqual(meta['aligned_to'], 'a')
        self.assertEqual(meta['alignment']['map_sha256'], c.sha256_file(root / 'symbol-map.tsv'))

    def test_regeneration_removes_stale_map_and_structure(self):
        root = self.ingest_fixture('b')
        (root / 'symbol-map.tsv').write_text('stale map')
        (root / 'structure').mkdir()
        (root / 'structure/stale.h').write_text('stale')
        with patch.object(av.subprocess, 'run', side_effect=self.fake_delinker):
            self.run_ingest('--force')
        self.assertFalse((root / 'symbol-map.tsv').exists())
        self.assertFalse((root / 'structure').exists())

    def test_failed_regeneration_removes_completion_metadata(self):
        root = self.ingest_fixture('b')
        with patch.object(av.subprocess, 'run', side_effect=subprocess.CalledProcessError(1, 'fixture')):
            with self.assertRaises(subprocess.CalledProcessError):
                self.run_ingest('--force')
        self.assertFalse((root / 'meta.json').exists())

    def test_chain_requires_missing_middle_build(self):
        self.ingest_fixture('a')
        self.ingest_fixture('c')
        with self.assertRaisesRegex(SystemExit, 'ingest: b'):
            cr.ingested_ordered()

    def test_chain_obeys_configured_order(self):
        self.ingest_fixture('a')
        self.ingest_fixture('b')
        c.CONFIG_PATH.write_text(json.dumps({'versions': ['b', 'a']}))
        self.assertEqual([v['label'] for v in cr.ingested_ordered()], ['b', 'a'])

    def test_symbol_less_build_cannot_enter_chain(self):
        self.entries[0]['symbols'] = False
        c.REGISTRY_PATH.write_text(json.dumps(self.entries))
        with self.assertRaisesRegex(SystemExit, 'not a PDB-bearing'):
            c.chain_versions()

    def cache_fixture(self):
        self.ingest_fixture('a')
        self.ingest_fixture('b')
        pair = self.diffs / 'a__b'
        pair.mkdir(parents=True)
        report = pair / 'report.json'
        report.write_text('{"units": []}')
        (pair / 'run.json').write_text(json.dumps({'inputs': c.comparison_inputs('a', 'b'),
                                                  'report_sha256': c.sha256_file(report)}))
        return report

    def test_valid_cache_is_reused(self):
        report = self.cache_fixture()
        with patch.object(cr.subprocess, 'run') as run:
            self.assertEqual(cr.ensure_report('a', 'b'), report)
            run.assert_not_called()

    def test_cache_invalidated_by_changed_objects_or_report(self):
        report = self.cache_fixture()
        (self.versions / 'b/objects/vostok/unit.obj').write_bytes(b'changed')
        with patch.object(cr.subprocess, 'run') as run:
            cr.ensure_report('a', 'b')
            run.assert_called_once()
        pair = report.parent
        (pair / 'run.json').write_text(json.dumps({'inputs': c.comparison_inputs('a', 'b'),
                                                 'report_sha256': c.sha256_file(report)}))
        report.write_text('{"units": [1]}')
        with patch.object(cr.subprocess, 'run') as run:
            cr.ensure_report('a', 'b')
            run.assert_called_once()

    def test_diff_writes_provenance_and_only_work_outputs(self):
        self.ingest_fixture('a')
        self.ingest_fixture('b')
        def run(args, **kwargs):
            Path(args[args.index('-o') + 1]).write_text(json.dumps({'units': []}))
        with patch.object(sys, 'argv', ['diff_versions.py', 'a', 'b']), patch.object(dv.subprocess, 'run', side_effect=run), contextlib.redirect_stdout(io.StringIO()):
            dv.main()
        pair = self.diffs / 'a__b'
        saved = json.loads((pair / 'run.json').read_text())
        self.assertEqual(saved['report_sha256'], c.sha256_file(pair / 'report.json'))
        self.assertEqual(saved['inputs'], c.comparison_inputs('a', 'b'))
        self.assertTrue((pair / 'objdiff.json').is_file())
        self.assertFalse((self.root / 'reports').exists())

    def test_fp_fast_is_reported_per_build(self):
        c.CONFIG_PATH.write_text(json.dumps({'versions': ['a', 'b']}))
        with patch.object(sys, 'argv', ['flags_report.py']), patch.object(fr, 'pdb_build_info', return_value='fixture'), patch.object(c, 'fetch_from_flake', return_value=self.source), patch.object(fr, 'project_configs', return_value={'vostok_test': '/MT -O1'}), patch.object(fr, 'changed_projects', return_value=[]), patch.object(fr, 'full_flag_projects', side_effect=[{'vostok_test'}, set()]), contextlib.redirect_stdout(io.StringIO()):
            fr.main()
        text = (self.reports / 'BUILD_FLAGS.md').read_text()
        self.assertIn('| `vostok_test` | a |', text)
        saved = json.loads((self.reports / 'BUILD_FLAGS.json').read_text())
        self.assertEqual(saved['builds']['b']['fp_fast_projects'], [])

    def test_markers_are_separate_from_declared_versions_and_imports(self):
        with patch.object(dr, 'exe_strings', return_value=['RTTI @boost@@', 'log mentions d3d11.dll']), patch.object(dr, 'v_bugtrap', return_value=None):
            result = dr.scan(self.source / 'survarium.exe', self.source)
        boost = result['dependencies']['boost']
        self.assertIsNone(boost['version_observation'])
        self.assertEqual(boost['declared_reference_version'], '1.48.0')
        self.assertEqual(dr.cell(boost), 'marker observed')
        self.assertIn('d3d11.dll', result['dll_name_markers'])
        self.assertNotIn('imports', result)

    def test_bad_cached_exe_hash_is_rejected(self):
        (self.catalog / 'extra_builds.json').write_text(json.dumps([{
            'label': 'v0.69d0-2022', 'exe_url': 'https://example.invalid/exe',
            'exe': 'input/survarium.exe', 'exe_sha256': 'sha256-' + base64.b64encode(b'\x00' * 32).decode(),
        }]))
        with patch.object(c, 'registry', return_value=[]), patch.object(sys, 'argv', ['deps_report.py']), patch.object(dr, 'scan') as scan:
            with self.assertRaisesRegex(SystemExit, 'hash mismatch'):
                dr.main()
            scan.assert_not_called()

    def test_relative_packaging_output_survives_temporary_directory_cleanup(self):
        tools = self.root / 'bin'
        tools.mkdir()
        sevenzip = tools / '7z'
        sevenzip.write_text(f'#!{sys.executable}\n' + '''import pathlib,sys
args=sys.argv[1:]
if args[0]=='l': print('Path = Collection/Build/game/binaries/x86/survarium.exe')
elif args[0] in ('e','x'):
 out=pathlib.Path(next(a[2:] for a in args if a.startswith('-o')))
 if args[0]=='e':
  out.mkdir(parents=True,exist_ok=True)
  (out/'survarium.exe').write_text('Vostok Engine v0.28a2\\nApr 24 2015\\n')
 else:
  (out/'Collection/Build').mkdir(parents=True,exist_ok=True)
  (out/'Collection/Build/file').write_text('fixture')
elif args[0]=='a':
 dest=pathlib.Path([a for a in args[1:] if not a.startswith('-')][0])
 dest.write_bytes(b'archive fixture')
''')
        sevenzip.chmod(0o755)
        strings = tools / 'strings'
        strings.write_text(f'#!{sys.executable}\nimport pathlib,sys\nprint(pathlib.Path(sys.argv[-1]).read_text())\n')
        strings.chmod(0o755)
        (self.root / 'input archive.zip').write_text('fixture')
        env = dict(os.environ, PATH=str(tools) + os.pathsep + os.environ['PATH'])
        subprocess.run([shutil.which('bash'), str(SCRIPTS / 'package_builds.sh'), 'input archive.zip', 'relative output'], cwd=self.root, env=env, check=True, capture_output=True)
        self.assertEqual(len(list((self.root / 'relative output').glob('*.zip'))), 1)
