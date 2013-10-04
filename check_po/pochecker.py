# -*- coding: utf-8 -*-
import sys
import os.path
import polib

from ._compat import writeout


def check_pofile(po_file):
    po = polib.pofile(po_file)

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
        writeout("Edit: %s\n\n" % os.path.abspath(
            getattr(po_file, 'name', 'stdin')))
        sys.exit(100)

    writeout("%s: PO File OK\n\n" % getattr(po_file, 'name', 'stdin'))


def main():
    if len(sys.argv) != 2:
        writeout("USAGE: %s <po_file_to_check>\n" % sys.argv[0])
        sys.exit(1)

    po_file = sys.argv[1]

    if not os.path.exists(po_file):
        writeout("File not found %s\n" % po_file)
        sys.exit(2)

    check_pofile(po_file)
    sys.exit(0)
