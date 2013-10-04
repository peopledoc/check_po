# -*- coding: utf-8 -*-
import unittest
import sys
from .._compat import StringIO

from ..pochecker import check_pofile, main


class CheckPoTestCase(unittest.TestCase):

    def test_noconflict(self):
        sys.stdout = StringIO()
        string = """
msgid "^request/$"
msgstr "^demande/$"

msgid "^requester/$"
msgstr "^demandeur/$"
"""
        check_pofile(string)
        self.assertEqual(sys.stdout.getvalue(), '''stdin: PO File OK


''')

    def test_untranslated(self):
        sys.stdout = StringIO()
        with self.assertRaises(SystemExit):
            check_pofile("""
msgid "^request/$"
msgstr ""

msgid "^requester/$"
msgstr "^demandeur/$"
""")
        self.assertTrue(sys.stdout.getvalue().startswith(
            '''UNTRANSLATED	 ^request/$

----------
1 UNTRANSLATED string found.
----------
Edit:'''))

    def test_fuzzy(self):
        sys.stdout = StringIO()
        with self.assertRaises(SystemExit):
            check_pofile("""
msgid "^request/$"
msgstr "^demande/$"

#, fuzzy
msgid "^requester/$"
msgstr "^demande/$"
""")
        self.assertTrue(sys.stdout.getvalue().startswith(
            '''FUZZY	 ^requester/$ ^demande/$

----------
1 FUZZY string found.
----------
Edit: '''))

    def test_cli_noargs(self):
        sys.argv = ['check_urls']
        sys.stdout = StringIO()
        with self.assertRaises(SystemExit) as cm:
            main()

        self.assertEqual(cm.exception.code, 1)

    def test_cli_wrong_args(self):
        sys.argv = ['check_urls', 'test.po']
        sys.stdout = StringIO()
        with self.assertRaises(SystemExit) as cm:
            main()

        self.assertEqual(cm.exception.code, 2)
