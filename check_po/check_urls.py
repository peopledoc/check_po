# -*- coding: utf-8 -*-
import sys
import os.path
import polib
from collections import defaultdict


def main():
    if len(sys.argv) < 2:
        writeout("USAGE: %s <po_files...>\n" % sys.argv[0])
        sys.exit(1)

    po_files = []

    # Open PO files
    for po_file_path in sys.argv[1:]:
        if not os.path.exists(po_file_path):
            writeout("File not found %s\n" % po_file_path)
            sys.exit(2)
        po_files.append(polib.pofile(po_file_path))

    # Check for duplicates
    entries = defaultdict(list)

    for po in po_files:
        for entry in po:
            msgid = entry.msgid.encode('utf-8')
            msgstr = entry.msgstr.encode('utf-8')

            if msgstr and entries[msgstr] and msgid not in entries[msgstr]:
                if msgid.startswith('^') and msgstr in entries:
                    writeout("DUPLICATE: %s" % msgstr)
                    for msg in entries[msgstr]:
                        writeout("\t\t\t%s" % msg)
                    writeout("\t\t\t%s\n" % msgid)
            entries[msgstr].append(msgid)

    sys.exit(0)

if __name__ == "__main__":
    main()
