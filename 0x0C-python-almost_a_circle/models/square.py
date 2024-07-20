#!/usr/bin/python3
""" Square module, defines a square. """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ The square class, contains square informations. """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
