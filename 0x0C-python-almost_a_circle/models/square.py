#!/usr/bin/python3
""" Square module, defines a square. """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ The square class, contains square informations. """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, val):
        self.width = val
        self.height = val

    def update(self, *args, **kwargs):
        """ Updates the current square. """
        if not args:
            for attr, val in kwargs.items():
                self.__setattr__(attr, val)
        try:
            self.id = args[0]
            self.size = args[1]
            self.x = args[2]
            self.y = args[3]
        except Exception:
            pass

    def to_dictionary(self):
        """ represent Rectangle in a dict. """
        return {'id': self.__getattribute__('id'),
                'size': self.__getattribute__('size'),
                'x': self.__getattribute__('x'),
                'y': self.__getattribute__('y')}
