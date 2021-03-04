import sys
import os.path
import polib


class PODiff:

    def __init__(self, file1, file2):
        self.po1 = polib.pofile(file1)
        self.po2 = polib.pofile(file2)

        self.entries = dict()
        self.entries2 = dict()

    def diff(self):
        for entry in self.po1:
            self.entries[entry.msgid] = entry.msgstr

        for entry in self.po2:
            self.entries2[entry.msgid] = entry.msgstr

        for msgid, msgstr in self.entries2.items():
            if msgid not in self.entries:
                print(f"NEW: {msgid}\n+ {msgstr}")
            else:
                if msgstr != self.entries[msgid]:
                    print(f"UPDATED: {msgid}\n"
                          f"- {self.entries[msgid]}\n"
                          f"+ {msgstr}")

        for msgid, msgstr in self.entries.items():
            if msgid not in self.entries2:
                print(f"DELETED: {msgid}\n- {msgstr}")


def main():
    if len(sys.argv) != 3:
        print(f"USAGE: {sys.argv[0]} po_file_v1 po_file_v2\n")
        sys.exit(1)

    po_file1_path = sys.argv[1]
    po_file2_path = sys.argv[2]

    if not os.path.exists(po_file1_path):
        print(f"File not found {po_file1_path}\n")
        sys.exit(2)

    if not os.path.exists(po_file2_path):
        print(f"File not found {po_file2_path}\n")
        sys.exit(3)

    podiff = PODiff(po_file1_path, po_file2_path)
    podiff.diff()

    sys.exit(0)


if __name__ == "__main__":
    main()
