import unittest
import sys
from io import StringIO

from ..check_urls import CheckURLs, main


class CheckURLsTestCase(unittest.TestCase):

    def test_nofile(self):
        self.urls_checker = CheckURLs()
        self.urls_checker.check_urls()

    def test_noconflict(self):
        sys.stdout = StringIO()
        self.urls_checker = CheckURLs(["""
msgid "^request/$"
msgstr "^demande/$"

msgid "^requester/$"
msgstr "^demandeur/$"
"""])
        self.urls_checker.check_urls()
        self.assertEqual(sys.stdout.getvalue(), '')

    def test_conflict(self):
        sys.stdout = StringIO()
        self.urls_checker = CheckURLs(["""
msgid "^request/$"
msgstr "^demande/$"

msgid "^requester/$"
msgstr "^demande/$"
"""])
        self.urls_checker.check_urls()
        self.assertEqual(sys.stdout.getvalue(), '''DUPLICATE: ^demande/$
\t\t\t^request/$
\t\t\t^requester/$

''')

    def test_cli_noargs(self):
        sys.argv = ['check_urls']
        sys.stdout = StringIO()
        with self.assertRaises(SystemExit) as cm:
            main()

        self.assertEqual(cm.exception.code, 1)
