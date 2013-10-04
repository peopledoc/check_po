# -*- coding: utf-8 -*-

import sys
import os.path
import polib


from .utils import writeout


def check_pofile(po_file_path):
    if not os.path.exists(po_file_path):
        writeout("File not found %s\n" % po_file_path)
        sys.exit(2)

    po = polib.pofile(po_file_path)

    UNTRANSLATED = 0
    for entry in po.untranslated_entries():
        UNTRANSLATED += 1
        writeout("UNTRANSLATED\t", entry.msgid)

    FUZZY = 0
    for entry in po.fuzzy_entries():
        FUZZY += 1
        writeout("FUZZY\t", entry.msgid, entry.msgstr)

    if FUZZY or UNTRANSLATED:
        writeout("\n----------")
        if FUZZY:
            writeout("%d FUZZY string found." % FUZZY)
        if UNTRANSLATED:
            writeout("%d UNTRANSLATED string found." % UNTRANSLATED)
        writeout("----------")
        writeout("Edit: %s\n\n" % os.path.abspath(po_file_path))
        sys.exit(100)

    writeout("%s: PO File OK\n\n" % po_file_path)
    sys.exit(0)


def main():
    if len(sys.argv) != 2:
        writeout("USAGE: %s <po_file_to_check>\n" % sys.argv[0])
        sys.exit(1)

    po_file_path = sys.argv[1]
    check_pofile(po_file_path)
