#!/usr/bin/python3
""" defines ``is_kind_of_class(...)`` function. """


def is_kind_of_class(obj, a_cls):
    """ checks if ``obj`` is an instance of ``a_cls``. """
    return isinstance(obj, a_cls)
