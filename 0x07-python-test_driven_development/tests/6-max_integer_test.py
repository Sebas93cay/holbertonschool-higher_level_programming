#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_maxnumber(self):
        self.assertAlmostEqual(max_integer([1, 2, 3]), 3)
        self.assertAlmostEqual(max_integer([1, 2, -3]), 2)
        self.assertAlmostEqual(max_integer([1, -2, -3, 0]), 1)
        self.assertAlmostEqual(max_integer([1, 2, -3]), 2)
        self.assertAlmostEqual(max_integer([1, 2, -30]), 2)
        self.assertAlmostEqual(max_integer([1, 2214, -3]), 2214)
        self.assertAlmostEqual(max_integer([-154, -9, -3]), -3)
        self.assertAlmostEqual(max_integer([1, 2, -30]), 2)
        self.assertAlmostEqual(max_integer([1234, 2, -30]), 1234)
        self.assertAlmostEqual(max_integer([-987, -34, -330]), -34)
        self.assertAlmostEqual(max_integer([1234, 2, -30, 45, 7566, 34]), 7566)
