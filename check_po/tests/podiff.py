# -*- coding: utf-8 -*-
import unittest
import sys
from .._compat import StringIO

from ..podiff import PoDiff, main


class PoDiffTestCase(unittest.TestCase):

    def test_noconflict(self):
        sys.stdout = StringIO()
        podiff = PoDiff("""
msgid "^request/$"
msgstr "^demande/$"

msgid "^requester/$"
msgstr "^demandeur/$"
""", """
msgid "^requester/$"
msgstr "^demandeur/$"

msgid "^request/$"
msgstr "^demande/$"
""")
        podiff.diff()
        self.assertEqual(sys.stdout.getvalue(), '')

    def test_diff(self):
        sys.stdout = StringIO()
        podiff = PoDiff("""
msgid "^request/$"
msgstr "^demande/$"

msgid "^requester/$"
msgstr "^demandeur/$"
""", """
msgid "^requester/$"
msgstr "^demandeur/$"

msgid "^request/$"
msgstr "^requete/$"
""")
        podiff.diff()
        self.assertEqual(sys.stdout.getvalue(),
                         '''UPDATED: ^request/$
- ^demande/$
+ ^requete/$)
''')

    def test_add(self):
        sys.stdout = StringIO()
        podiff = PoDiff("""
msgid "^requester/$"
msgstr "^demandeur/$"
""", """
msgid "^requester/$"
msgstr "^demandeur/$"

msgid "^request/$"
msgstr "^requete/$"
""")
        podiff.diff()
        self.assertEqual(sys.stdout.getvalue(),
                         '''NEW: ^request/$
+ ^requete/$
''')

    def test_deleted(self):
        sys.stdout = StringIO()
        podiff = PoDiff("""
msgid "^request/$"
msgstr "^requete/$"

msgid "^requester/$"
msgstr "^demandeur/$"
""", """
msgid "^requester/$"
msgstr "^demandeur/$"
""")
        podiff.diff()
        self.assertEqual(sys.stdout.getvalue(),
                         '''DELETED : ^request/$
- ^requete/$
''')

    def test_cli_noargs(self):
        sys.argv = ['podiff']
        sys.stdout = StringIO()
        with self.assertRaises(SystemExit) as cm:
            main()

        self.assertEqual(cm.exception.code, 1)
