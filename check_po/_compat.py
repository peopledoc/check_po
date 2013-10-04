# -*- coding: utf-8 -*-
from __future__ import print_function
import sys

PY2 = sys.version_info[0] == 2

if PY2:
    from cStringIO import StringIO
else:
    from io import StringIO  # NOQA


def writeout(*args):
    """Wrapper around 'print' for Py2/3 _compatibility."""
    if PY2:
        # Need to send 'bytes' to print on Py2
        args = [arg.encode('utf-8') for arg in args]
    print(*args)


def encode(string):
    """Wrapper around 'print' for Py2/3 _compatibility."""
    if PY2:
        return string.encode('utf-8')
    return string


def items(dictionnary):
    if PY2:
        return dictionnary.iteritems()
    else:
        return dictionnary.items()
