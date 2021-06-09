#!/usr/bin/python3
"""
Test differents behaviors of the Base class
"""
import unittest
import pep8
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """
    A class to test Base Class
    """

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

    def test_id_as_positive(self):
        """
        Test for positive Base Class id
        """
        base_instance = Base(110)
        self.assertEqual(base_instance.id, 110)
        base_instance = Base(30)
        self.assertEqual(base_instance.id, 30)
