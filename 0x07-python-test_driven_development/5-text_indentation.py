#!/usr/bin/python3
""" text_indentation. """


def text_indentation(text):
    """ prints a text with 2 new lines after each of these characters:
        - .
        - ?
        - :
    """
    special = ['.', '?', ':']
    i = 0
    if type(text) is not str:
        raise TypeError('text must be a string')
    while i < len(text):
        print(text[i], end='')
        if text[i] in special:
            print('\n')
            j = i + 1
            while j < len(text):
                if text[j] != ' ':
                    break
                j += 1
            i = j - 1
        i += 1
