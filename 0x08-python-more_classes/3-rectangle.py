#!/usr/bin/python3
""" Defines a simple rectangle. """


class Rectangle:
    """ Rectangles object proporties & infos. """
    def __init__(self, width=0, height=0):
        """ Initializing the instance """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError('width must be >= 0')
        self.__width = width

        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError('height must be >= 0')
        self.__height = height

    @property
    def width(self):
        """ width getter. """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter. """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """ height getter. """
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter. """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """ Computes the area of the current rectangle.
        Returns:
            the results.
        """
        return self.__width * self.__height

    def perimeter(self):
        """ Computes the perimeter of the current rectangle.
        Returns:
            the results.
        """
        if self.__height and self.__width:
            return (self.__width + self.__height) * 2
        else:
            return 0

    def __str__(self):
        h = 0
        tmp = ""
        if self.__width and self.height:
            while self.height > h:
                tmp += (("#" * self.__width) +
                        ('\n' if h + 1 < self.height else ''))
                h += 1
            return tmp
        else:
            return ""
