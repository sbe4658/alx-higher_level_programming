#!/usr/bin/python3
""" Geometry module. """


class BaseGeometry:
    """ Geometry parent class. """
    def area(self):
        raise Exception('area() is not implemented')
