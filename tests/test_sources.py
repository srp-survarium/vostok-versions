import contextlib
import hashlib
import io
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import fetch_update_notes as fetch  # noqa: E402


class SourceTests(unittest.TestCase):
    def test_category_pagination(self):
        with patch.object(fetch, 'api_query', side_effect=[
            {'query': {'categorymembers': [{'title': '0.1'}]},
             'continue': {'cmcontinue': 'next', 'continue': '-||'}},
            {'query': {'categorymembers': [{'title': '0.2'}]}},
        ]) as query:
            self.assertEqual(len(fetch.category_members(fetch.ROOT_CATEGORY)), 2)
        self.assertEqual(query.call_args.kwargs['cmcontinue'], 'next')

    def test_page_link_pagination_keeps_first_revision(self):
        with patch.object(fetch, 'api_query', side_effect=[
            {'query': {'pages': {'1': {'title': '0.1', 'revisions': ['first'],
                                      'links': [{'ns': 0, 'title': '0.2'}]}}},
             'continue': {'plcontinue': 'next'}},
            {'query': {'pages': {'1': {'title': '0.1',
                                      'links': [{'ns': 0, 'title': '0.3'},
                                                {'ns': 0, 'title': 'Weapon'}]}}}},
        ]):
            page = fetch.fetch_page('0.1')
        self.assertEqual(page['version_links'], ['0.2', '0.3'])
        self.assertEqual(page['revisions'], ['first'])

    def test_collection_follows_links_records_missing_and_refuses_overwrite(self):
        content = '{{Infobox version\n|date = 1 April 2015\n}}\nUnchanged text.\n'

        def page(title):
            if title == '0.2':
                return {'title': title, 'missing': '', 'version_links': []}
            return {'title': title, 'pageid': 1,
                    'version_links': ['0.2'] if title == '0.1' else [],
                    'revisions': [{'revid': 2, 'timestamp': '2015-04-01T00:00:00Z',
                                   'user': 'Fixture', 'slots': {'main': {'*': content}}}]}

        def members(title):
            if title == fetch.ROOT_CATEGORY:
                return [{'ns': 14, 'title': 'Category:Major'}]
            return [{'ns': 0, 'title': '0.1'}]

        with tempfile.TemporaryDirectory() as temp:
            output = Path(temp) / 'snapshot'
            with patch.object(sys, 'argv', ['fetch', '--output', str(output)]), \
                 patch.object(fetch, 'api_query', return_value={'query': {'rightsinfo': {'text': 'fixture'}}}), \
                 patch.object(fetch, 'category_members', side_effect=members), \
                 patch.object(fetch, 'fetch_page', side_effect=page), \
                 contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
                fetch.main()
                manifest = json.loads((output / 'manifest.json').read_text())
                records = {p['title']: p for p in manifest['pages']}
                self.assertEqual(records['0.2']['status'], 'missing')
                self.assertEqual((output / records['0.1']['path']).read_text(), content)
                self.assertFalse((output / 'INCOMPLETE').exists())
                with self.assertRaises(SystemExit):
                    fetch.main()
                self.assertEqual(json.loads((output / 'manifest.json').read_text()), manifest)

    def test_preserved_research_snapshot_hashes(self):
        snapshot = ROOT / 'reports/2026-06'
        manifest = json.loads((snapshot / 'manifest.json').read_text())
        for record in manifest['files']:
            with self.subTest(path=record['path']):
                self.assertEqual(hashlib.sha256((snapshot / record['path']).read_bytes()).hexdigest(),
                                 record['sha256'])

    def test_wiki_snapshot_hashes_and_coverage(self):
        snapshot = ROOT / 'sources/fandom-updates/2026-09-12'
        manifest = json.loads((snapshot / 'manifest.json').read_text())
        records = {p['title']: p for p in manifest['pages']}
        categories = json.loads((snapshot / 'categories.json').read_text())
        for members in categories.values():
            for member in members:
                if member['ns'] in (0, 14):
                    self.assertIn(member['title'], records)
        for record in records.values():
            for linked in record['version_links']:
                self.assertIn(linked, records)
            if record['status'] == 'captured':
                self.assertEqual(hashlib.sha256((snapshot / record['path']).read_bytes()).hexdigest(),
                                 record['sha256'])
        self.assertEqual([p['title'] for p in records.values() if p['status'] == 'missing'], ['0.28d'])
        self.assertEqual(sum(p['status'] == 'captured' and bool(fetch.VERSION_TITLE.fullmatch(p['title']))
                             for p in records.values()), 91)
