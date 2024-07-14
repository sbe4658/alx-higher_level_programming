#!/usr/bin/python3
""" defines ``inherits_from(...)`` function. """


def inherits_from(obj, a_cls):
    """ checks if ``obj`` is an inherited instance of ``a_cls``. """
    return issubclass(type(obj), a_cls) and type(obj) is not a_cls
