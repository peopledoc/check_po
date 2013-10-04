# -*- coding: utf-8 -*-
import sys
import os.path
import polib


def main():
    if len(sys.argv) != 3:
        writeout("USAGE: %s po_file_v1 po_file_v2\n" % sys.argv[0])
        sys.exit(1)

    po_file1_path = sys.argv[1]
    po_file2_path = sys.argv[2]

    if not os.path.exists(po_file1_path):
        writeout("File not found %s\n" % po_file1_path)
        sys.exit(2)

    if not os.path.exists(po_file2_path):
        writeout("File not found %s\n" % po_file2_path)
        sys.exit(3)

    po1 = polib.pofile(po_file1_path)
    po2 = polib.pofile(po_file2_path)

    ENTRIES = {}

    for entry in po1:
        ENTRIES[entry.msgid.encode('utf-8')] = entry.msgstr.encode('utf-8')

    ENTRIES2 = {}
    for entry in po2:
        ENTRIES2[entry.msgid.encode('utf-8')] = entry.msgstr.encode('utf-8')

    for msgid, msgstr in ENTRIES2.iteritems():
        if msgid not in ENTRIES:
            writeout("NEW: %s\n+ %s" % (msgid, msgstr))
        else:
            if msgstr != ENTRIES[msgid]:
                writeout("UPDATED: %s\n- %s\n+ %s)" % (
                    msgid,
                    ENTRIES[msgid].decode('utf-8'),
                    msgstr.encode('utf-8'))
                )

    for msgid, msgstr in ENTRIES.iteritems():
        if msgid not in ENTRIES2:
            writeout("DELETED : %s\n- %s" % (msgid, msgstr))
    sys.exit(0)

if __name__ == "__main__":
    main()
