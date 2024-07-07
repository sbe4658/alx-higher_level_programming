#!/usr/bin/python3
"""Defines a square."""


class Square:
    """The object of the square."""
    def __init__(self, size=0):
        """Initialization.
        Args:
            size: private instance attribute.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Public instance methode.

        Returns:
            The area of the current square.
        """
        return self.__size ** 2

    @property
    def size(self):
        """size getter.
        Returns:
            the size of the current square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """size setter.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
