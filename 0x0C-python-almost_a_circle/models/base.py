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

    @classmethod
    def create(cls, **dictonary):
        """ Creates a dummy instance, and then use the update methed
            on the list of dicts.
        """
        from models.rectangle import Rectangle
        from models.square import Square
        obj = cls.__name__
        if obj == 'Square':
            dummy = Square(2)
        elif obj == 'Rectangle':
            dummy = Rectangle(3, 4)
        dummy.update(**dictonary)
        return dummy

    @classmethod
    def save_to_file(cls, list_objs):
        to_write = []
        if list_objs is not None:
            for instance in list_objs:
                json_encode = instance.to_dictionary()
                to_write.append(json_encode)
        with open(f'{cls.__name__}.json', 'w') as f:
            f.write(cls.to_json_string(to_write))

    @classmethod
    def load_from_file(cls):
        """ returns a list of instaces. """
        try:
            with open(f'{cls.__name__}.json') as f:
                data = cls.from_json_string(f.read())
        except Exception:
            return []
        instances = []
        for dict in data:
            instances.append(cls.create(**dict))
        return instances

    @staticmethod
    def from_json_string(json_string):
        if json_string is None:
            return []
        return json.loads(json_string)

    @staticmethod
    def to_json_string(list_dictionaries):
        """ encode a list of dicts. in json. """
        if list_dictionaries is None:
            return '[]'
        return json.dumps(list_dictionaries)
