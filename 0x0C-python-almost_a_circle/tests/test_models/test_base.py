#!/usr/bin/python3
"""This module has the test for the base class"""
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle
import unittest
import os
import pep8


class testBase(unittest.TestCase):
    """test for base class"""

    def setUp(self):
        """set up for every test"""
        super().setUp()
        Base._Base__nb_objects = 0

    def test_pep8_base(self):
        """
        Test that checks PEP8
        """
        syntax = pep8.StyleGuide(quit=True)
        check = syntax.check_files(['models/base.py'])
        self.assertEqual(
            check.total_errors, 0,
            "Found code style errors (and warnings)."
        )

    def test_init(self):
        """test init"""
        b1 = Base()
        b2 = Base()
        self.assertEqual(1, b1.id)
        self.assertEqual(b2.id, 2)
        b3 = Base()
        b4 = Base(34)
        b5 = Base()
        self.assertEqual(b3.id, 3)
        self.assertEqual(b4.id, 34)
        self.assertEqual(b5.id, 4)
