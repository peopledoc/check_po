import sys
import polib
from collections import defaultdict


class CheckURLs:
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
            msgid = entry.msgid
            msgstr = entry.msgstr

            if msgstr and self.entries[msgstr] \
                    and msgid not in self.entries[msgstr]:
                if msgid.startswith('^') and msgstr in self.entries:
                    print(f"DUPLICATE: {msgstr}")
                    for msg in self.entries[msgstr]:
                        print(f"\t\t\t{msg}")
                    print(f"\t\t\t{msgid}\n")
            self.entries[msgstr].append(msgid)

    def check_urls(self):
        """Check urls for all files."""
        for f in self.files:
            self.check_other_file(f)


def main():
    if len(sys.argv) < 2:
        print(f"USAGE: {sys.argv[0]} <po_files...>\n")
        sys.exit(1)

    url_checker = CheckURLs(sys.argv[1:])
    url_checker.check_urls()

    sys.exit(0)


if __name__ == "__main__":
    main()
