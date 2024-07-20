#!/usr/bin/python3
""" Rectangle module. and Rectangle is documented?"""
from models.base import Base


class Rectangle(Base):
    """ Rectangle objects, defines rect. informations. """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

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
        """ Computes the area of the current rectangle. """
        return self.__height * self.__width

    def display(self):
        """ Prints the current Rectangle. """
        w = self.width
        h = self.height
        for i in range(0, self.y):
            print()
        while h > 0:
            print(' ' * self.x, end='')
            print('#' * w)
            h -= 1

    def update(self, *args):
        try:
            self.id = args[0]
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        except Exception:
            pass

    def __str__(self):
        """ Return a string. """
        return '[Rectangle] ({:}) {}/{} - {}/{}'.format(self.id, self.x,
                                                        self.y, self.width,
                                                        self.height)
