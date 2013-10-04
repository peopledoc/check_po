# -*- coding: utf-8 -*-

from __future__ import print_function


import sys


def writeout(*args):
    """Wrapper around 'print' for Py2/3 compatibility."""
    if sys.version_info[0] == 2:
        # Need to send 'bytes' to print on Py2
        args = [arg.encode('utf-8') for arg in args]
    print(*args)


def encode(string):
    """Wrapper around 'print' for Py2/3 compatibility."""
    if sys.version_info[0] == 2:
        return string.encode('utf-8')
    return string
