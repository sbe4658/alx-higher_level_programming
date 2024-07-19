#!/usr/bin/python3
""" Tests Rectangle. """
from models.rectangle import Rectangle
import unittest

class  TestRectangle(unittest.TestCase):
    """ Testing Rectangle class. """
    def test_rect_id(self):
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 2)
        r3 = Rectangle(2, 10, 0, 0, 12)
        self.assertEqual(r3.id, 12)
