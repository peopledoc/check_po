import sys
import os.path
import polib


def check_pofile(po_file):
    po = polib.pofile(po_file)
    filename = getattr(po_file, 'name', 'stdin')
    filepath = os.path.abspath(filename)

    UNTRANSLATED = 0
    for entry in po.untranslated_entries():
        UNTRANSLATED += 1
        print("UNTRANSLATED\t", entry.msgid)

    FUZZY = 0
    for entry in po.fuzzy_entries():
        FUZZY += 1
        print("FUZZY\t", entry.msgid, entry.msgstr)

    if FUZZY or UNTRANSLATED:
        print("\n----------")
        if FUZZY:
            print(f"{FUZZY} FUZZY string found.")
        if UNTRANSLATED:
            print(f"{UNTRANSLATED} UNTRANSLATED string found.")
        print("----------")
        print(f"Edit: {filepath}\n\n")
        sys.exit(100)

    print(f"{filename}: PO File OK\n\n")


def main():
    if len(sys.argv) != 2:
        print(f"USAGE: {sys.argv[0]} <po_file_to_check>\n")
        sys.exit(1)

    po_file = sys.argv[1]

    if not os.path.exists(po_file):
        print(f"File not found {po_file}\n")
        sys.exit(2)

    check_pofile(po_file)
    sys.exit(0)
