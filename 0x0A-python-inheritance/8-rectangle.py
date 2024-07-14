#!/usr/bin/python3
""" Geometry module. """


class BaseGeometry:
    """ Geometry parent class. """
    def area(self):
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError('{:s} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{:s} must be greater than 0'.format(name))


class Rectangle(BaseGeometry):
    """ defines a rectangle. """
    def __init__(self, w, h):
        self.integer_validator('width', w)
        self.integer_validator('height', h)
        self.__height = h
        self.__width = w
