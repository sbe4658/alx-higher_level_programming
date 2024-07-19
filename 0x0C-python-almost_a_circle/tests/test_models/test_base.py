#!/usr/bin/python3
import unittest
from models.base import Base
""" Neat!. """


class TestBase(unittest.TestCase):
    """ Tests the base.py. """
    def test_id(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)
        b2 = Base()
        self.assertEqual(b2.id, 2)
        b3 = Base(45)
        self.assertEqual(b3.id, 45)
        b4 = Base()
        self.assertEqual(b4.id, 3)
