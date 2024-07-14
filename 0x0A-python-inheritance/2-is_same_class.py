#!/usr/bin/python3
""" defines ``is_same_class(...)`` function. """


def is_same_class(obj, a_cls):
    """ checks if ``obj`` is an instance of ``a_cls``. """
    return obj.__class__ is a_cls
