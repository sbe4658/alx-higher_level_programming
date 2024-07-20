#!/usr/bin/python3
""" Base Class. """
import json


class Base:
    """ Base class, manages the ``id`` attribute. """
    __nb_objects = 0

    def __init__(self, id=None):
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ encode a list of dicts. in json. """
        if list_dictionaries:
            return json.dumps(list_dictionaries)
        else:
            return []
