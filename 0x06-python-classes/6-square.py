#!/usr/bin/python3
"""Defines a square."""


class Square:
    """The object of the square."""
    def __init__(self, size=0, position=(0, 0)):
        """Initialization.
        Args:
            size: private instance attribute.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        if (not isinstance(position, tuple) or len(position) != 2 or not
                all(map(lambda n: isinstance(n, int) and n >= 0, position))):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__size = size
        self.position = position

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
        """size setter."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """position getter."""
        return self.__position

    @position.setter
    def position(self, value):
        """position setter"""
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(map(lambda n: isinstance(n, int) and n >= 0, value))):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        s = 0
        print('\n' * self.__position[1], end='')
        while self.__size > s:
            print(' ' * (self.__position[0] - 1), "#" * self.__size)
            s += 1
        if self.__size == 0:
            print()
