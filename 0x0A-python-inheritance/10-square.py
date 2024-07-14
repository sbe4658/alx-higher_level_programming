#!/usr/bin/python3
""" Square module. """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ defines a square. """
    def __init__(self, size):
        self.__size = size
        super.__init__(self.__size, self.__size)
