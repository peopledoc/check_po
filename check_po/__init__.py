import sys
import os.path
import polib



def check_pofile(po_file_path):
    if not os.path.exists(po_file_path):
        print "File not found %s\n" % po_file_path
        sys.exit(2)

    po = polib.pofile(po_file_path)

    UNTRANSLATED = 0
    for entry in po.untranslated_entries():
        UNTRANSLATED += 1
        print "UNTRANSLATED\t", entry.msgid.encode('utf-8')

    FUZZY = 0
    for entry in po.fuzzy_entries():
        FUZZY += 1
        print "FUZZY\t", entry.msgid.encode('utf-8'), entry.msgstr.encode('utf-8')

    if FUZZY or UNTRANSLATED:
        print '\n----------'
        if FUZZY:
            print "%d FUZZY string found." % FUZZY
        if UNTRANSLATED:
            print "%d UNTRANSLATED string found." % UNTRANSLATED
        print '----------'
        print "Edit: %s\n\n" % os.path.abspath(po_file_path)
        sys.exit(100)

    print "%s: PO File OK\n\n" % po_file_path
    sys.exit(0)


def main():
    if len(sys.argv) != 2:
        print "USAGE: %s <po_file_to_check>\n" % sys.argv[0]
        sys.exit(1)

    po_file_path = sys.argv[1]
    check_pofile(po_file_path)
