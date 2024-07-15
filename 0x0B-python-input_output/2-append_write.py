#!/usr/bin/python3
""" Append text file. """


def append_write(filename="", txt=''):
    """Append to file. """
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(txt)
