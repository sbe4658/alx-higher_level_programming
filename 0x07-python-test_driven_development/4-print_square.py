#!/usr/bin/python3
""" prints square."""


def print_square(size):
    """Prints the square using the ``#`` symbol. """
    # logical err, doing what the task says so.
    if (type(size) is not int or
            (type(size) is float and size < 0)):
        raise TypeError('size must be an integer')
    elif size < 0:
        raise ValueError('size must be >= 0')
    tmp = size
    while tmp:
        print("#" * size)
        tmp -= 1
