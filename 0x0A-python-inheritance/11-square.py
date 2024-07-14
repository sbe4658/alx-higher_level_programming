#!/usr/bin/python3
""" Square module. """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ defines a square. """
    def __init__(self, size):
        super().__init__(size, size)
        self.__size = size
