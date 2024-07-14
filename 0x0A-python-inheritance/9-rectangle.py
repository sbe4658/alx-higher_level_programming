#!/usr/bin/python3
""" Rectangle module. """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ defines a rectangle. """
    def __init__(self, width, height):
        if width != height:
            self.integer_validator("width", width)
            self.integer_validator("height", height)
        else:
            self.integer_validator("size", height)

        self.__height = height
        self.__width = width

    def area(self):
        return self.__height * self.__width

    def __str__(self):
        if self.__height != self.__width:
            return f"[Rectangle] {self.__width}/{self.__height}"
        else:
            return f"[Square] {self.__width}/{self.__height}"
