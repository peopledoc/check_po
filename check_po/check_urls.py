# -*- coding: utf-8 -*-
import sys
import polib
from collections import defaultdict

from ._compat import encode, writeout


class CheckUrls(object):
    def __init__(self, files=None):
        if files is None:
            files = []

        self.files = []
        for f in files:
            self.add_file(f)

        self.entries = defaultdict(list)

    def add_file(self, f):
        """Add a file in the list of pofile to check."""
        self.files.append(polib.pofile(f))

    def check_other_file(self, po):
        """Check a po file against already checked files."""
        for entry in po:
            msgid = encode(entry.msgid)
            msgstr = encode(entry.msgstr)

            if msgstr and self.entries[msgstr] \
                    and msgid not in self.entries[msgstr]:
                if msgid.startswith('^') and msgstr in self.entries:
                    writeout("DUPLICATE: %s" % msgstr)
                    for msg in self.entries[msgstr]:
                        writeout("\t\t\t%s" % msg)
                    writeout("\t\t\t%s\n" % msgid)
            self.entries[msgstr].append(msgid)

    def check_urls(self):
        """Check urls for all files."""
        for f in self.files:
            self.check_other_file(f)


def main():
    if len(sys.argv) < 2:
        writeout("USAGE: %s <po_files...>\n" % sys.argv[0])
        sys.exit(1)

    url_checker = CheckUrls(sys.argv[1:])
    url_checker.check_urls()

    sys.exit(0)


if __name__ == "__main__":
    main()
