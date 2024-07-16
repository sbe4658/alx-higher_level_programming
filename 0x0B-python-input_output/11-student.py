#!/usr/bin/python3
""" Defines strundent class. """


class Student:
    """ Student class. """
    def __init__(self, first_name, last_name, age):
        """ initialize. """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attr=None):
        """ Converts to a dictionary. """
        a = {}
        if type(attr) is list:
            for attribute in attr:
                if hasattr(self, attribute):
                    a.update({attribute: getattr(self, attribute)})
        else:
            a = self.__dict__
        return a

    def reload_from_json(self, json):
        for attr in json.keys():
            setattr(self, attr, json.get(attr))
