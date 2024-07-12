#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ Edges cases for max_integer([..]). """
    def test_max_infront(self):
        test = [10, 5, 3]
        self.assertEqual(max_integer(test), 10)

    def test_max_end(self):
        test = [10, 5, 13]
        self.assertEqual(max_integer(test), 13)

    def test_max_middle(self):
        test = [10, 15, 3]
        self.assertEqual(max_integer(test), 15)

    def test_empty_list(self):
        self.assertIs(max_integer([]), None)

    def test_normal(self):
        test = [45, 102, 456, 7895]
        self.assertEqual(max_integer(test), 7895)

    def test_one_element(self):
        test = [0]
        self.assertEqual(max_integer(test), 0)

    def test_combination(self):
        test = [-1, 1.6, 5, 0]
        self.assertEqual(max_integer(test), 5)


if __name__ == '__main__':
    unittest.main()
