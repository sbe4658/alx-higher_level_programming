#!/usr/bin/python3
""" Defines strundent class. """


class Student:
    """ Student class. """
    def __init__(self, first_name, last_name, age):
        """ initialize. """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Converts to a dictionary. """
        return self.__dict__
