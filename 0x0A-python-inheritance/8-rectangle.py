#!/usr/bin/python3
""" Rectangle module. """
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """ defines a rectangle. """
    def __init__(self, w, h):
        self.integer_validator('width', w)
        self.integer_validator('height', h)
        self.__height = h
        self.__width = w
