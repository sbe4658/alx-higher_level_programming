#!/usr/bin/python3
""" Additiion of two numbers. """


def add_integer(a, b=98):
    """ Adds Two numbers.
    Args:
        a: requierd argument.
        b: optional argument, 98 if not passed.
    Raises:
        TypeError if a or b are not integers or floating points.
    Returns:
        a + b, casted to int type if they're floats.
    """
    if (type(a) is not int and type(a) is not float):
        raise TypeError('a must be an integer')
    if (type(b) is not int and type(b) is not float):
        raise TypeError('b must be an integer')
    return int(a) + int(b)
