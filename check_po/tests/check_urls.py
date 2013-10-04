# -*- coding: utf-8 -*-
import unittest
import sys
from .._compat import StringIO

from ..check_urls import CheckUrls, main


class CheckUrlsTestCase(unittest.TestCase):

    def test_nofile(self):
        self.urls_checker = CheckUrls()
        self.urls_checker.check_urls()

    def test_noconflict(self):
        sys.stdout = StringIO()
        self.urls_checker = CheckUrls(["""
msgid "^request/$"
msgstr "^demande/$"

msgid "^requester/$"
msgstr "^demandeur/$"
"""])
        self.urls_checker.check_urls()
        self.assertEqual(sys.stdout.getvalue(), '')

    def test_conflict(self):
        sys.stdout = StringIO()
        self.urls_checker = CheckUrls(["""
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
