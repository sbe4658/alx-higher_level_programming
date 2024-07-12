#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ Edges cases for max_integer([..]). """
    def empty_list(self):
        self.assertIs(max_integer([]), None)

    def normal(self):
        test = [45, 102, 456, 7895]
        self.assertEqual(max_integer(test), 7895)

    def one_element(self):
        test = [0]
        self.assertEqual(max_integer(test), 0)

    def combination(self):
        test = [-1, 1.6, 5, 0]
        self.assertEqual(max_integer(test), 5)


if __name__ == '__main__':
    unittest.main()
