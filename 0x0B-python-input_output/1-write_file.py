#!/usr/bin/python3
""" Write to file. """


def write_file(filename="", txt=''):
    """ Writes to a file. """
    with open(filename, 'w', encoding='utf-8') as f:
        c = f.write(txt)
    return c
