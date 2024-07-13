#!/usr/bin/python3
""" Definesa class, dynamic instance attribute creation prevention. """


class LockedClass():
    """ first_name is the way to unlock. """
    __slots__ = ['first_name']
