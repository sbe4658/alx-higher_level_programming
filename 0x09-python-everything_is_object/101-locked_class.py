#!/usr/bin/python3
""" Definesa class, dynamic instance attribute creation prevention. """


class LockedClass():
    """ first_name is the way to unlock. """
    __slot__ = ['first_name']
