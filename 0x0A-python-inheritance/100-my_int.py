#!/usr/bin/python3
""" my_int module. """


class MyInt(int):
    """ defines a square. """
    def __eq__(self, num):
        return num != self.real

    def __ne__(self, num):
        return num == self.real
