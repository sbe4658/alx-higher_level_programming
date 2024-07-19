#!/usr/bin/python3
""" Tests Rectangle. """
from models.rectangle import Rectangle
import unittest


class TestRectangle(unittest.TestCase):
    """ Testing Rectangle class. """
    def test_rect_id(self):
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 2)
        r3 = Rectangle(2, 10, 0, 0, 12)
        self.assertEqual(r3.id, 12)

    def test_validator(self):
        Rectangle("12", 13)
        self.assertRaises(TypeError)
        r1 = Rectangle(1, 2, 5, 6)
        r1.width = "Not value"
        self.assertRaises(TypeError)
        r1.height = "15"
        self.assertRaises(TypeError)
        r1.x = (1, '1')
        self.assertRaises(TypeError)
        r1.y = ['a']
        self.assertRaises(TypeError)
        r1.x = -1
        self.assertRaises(ValueError)
        r1.y = -5
        self.assertRaises(ValueError)
        r1.width = -1
        self.assertRaises(ValueError)
        r1.height = 0
        self.assertRaises(ValueError)
