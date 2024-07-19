#!/usr/bin/python3
""" Rectangle module. and Rectangle is documented?"""
from models.base import Base


class Rectangle(Base):
    """ Rectangle objects, defines rect. informations. """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        if type(width) is not int:
            raise TypeError('width must be an integer')
        elif type(height) is not int:
            raise TypeError('height must be an integer')
        elif type(x) is not int:
            raise TypeError('x must be an integer')
        elif type(y) is not int:
            raise TypeError('y must be an integer')
        if width <= 0:
            raise ValueError('width must be > 0')
        elif height <= 0:
            raise ValueError('height must be > 0')
        elif x < 0:
            raise ValueError('x must be >= 0')
        elif y < 0:
            raise ValueError('y must be >= 0')
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, val):
        if type(val) is not int:
            raise TypeError('width must be an integer')
        elif val <= 0:
            raise ValueError('width must be > 0')
        self.__width = val

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, val):
        if type(val) is not int:
            raise TypeError('height must be an integer')
        elif val <= 0:
            raise ValueError('height must be > 0')
        self.__height = val

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, val):
        if type(val) is not int:
            raise TypeError('x must be an integer')
        elif val < 0:
            raise ValueError('x must be >= 0')
        self.__x = val

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, val):
        if type(val) is not int:
            raise TypeError('y must be an integer')
        elif val < 0:
            raise ValueError('y must be >= 0')
        self.__y = val

    def area(self):
        return self.__height * self.__width
