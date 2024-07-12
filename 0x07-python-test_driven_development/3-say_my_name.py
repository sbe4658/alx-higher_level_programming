#!/usr/bin/python3
""" - Say My Name!
    - heisenberg
    - You're God d*me right!
"""


def say_my_name(first_name, last_name=""):
    """ Says your name. """
    if type(first_name) is not str:
        raise TypeError('first_name must be a string')
    if type(last_name) is not str:
        raise TypeError('last_name must be a string')
    print("My name is {:s} {:s}".format(first_name, last_name))
