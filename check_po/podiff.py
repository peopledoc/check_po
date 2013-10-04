# -*- coding: utf-8 -*-
import sys
import os.path
import polib
from ._compat import writeout, encode, items


class PoDiff(object):

    def __init__(self, file1, file2):
        self.po1 = polib.pofile(file1)
        self.po2 = polib.pofile(file2)

        self.entries = dict()
        self.entries2 = dict()

    def diff(self):
        for entry in self.po1:
            self.entries[encode(entry.msgid)] = encode(entry.msgstr)

        for entry in self.po2:
            self.entries2[encode(entry.msgid)] = encode(entry.msgstr)

        for msgid, msgstr in items(self.entries2):
            if msgid not in self.entries:
                writeout("NEW: %s\n+ %s" % (msgid, msgstr))
            else:
                if msgstr != self.entries[msgid]:
                    writeout(u"UPDATED: %s\n- %s\n+ %s)" % (
                        msgid,
                        self.entries[msgid],
                        encode(msgstr))
                    )

        for msgid, msgstr in items(self.entries):
            if msgid not in self.entries2:
                writeout("DELETED : %s\n- %s" % (msgid, msgstr))


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

    podiff = PoDiff(po_file1_path, po_file2_path)
    podiff.diff()

    sys.exit(0)


if __name__ == "__main__":
    main()
