#!/usr/bin/python3
""" Defines a simple rectangle. """


class Rectangle:
    """ Rectangles object proporties & infos. """
    number_of_instances = 0
    print_symbol = '#'

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
        Rectangle.number_of_instances += 1

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
        """ prints the current rectangle. """
        h = 0
        tmp = ""
        if self.__width and self.height:
            while self.height > h:
                tmp += ((str(self.print_symbol) * self.__width) +
                        ('\n' if h + 1 < self.height else ''))
                h += 1
            return tmp
        else:
            return ""

    def __repr__(self):
        """ reprisentation. """
        return f"Rectangle({self.__width:d}, {self.__height:d})"

    def __del__(self):
        """ farewell. """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if type(rect_1) is not Rectangle:
            raise TypeError('rect_1 must be an instance of Rectangle')
        if type(rect_2) is not Rectangle:
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """ Square is a Rectangle. """
        return cls(size, size)
