#!/usr/bin/python3

from io import StringIO
from models.square import Square
from models.base import Base
import unittest
from unittest.mock import patch


class testSquare(unittest.TestCase):
    def setUp(self):
        super().setUp()
        Base._Base__nb_objects = 0

    def test_init(self):
        # test rectangles id's
        r1 = Square(10, 2)
        self.assertEqual(r1.id, 1)

        r2 = Square(2, 10)
        self.assertEqual(r2.id, 2)

        r3 = Square(10, 2, 0, 112)
        self.assertEqual(r3.id, 112)

        r4 = Square(2, 2, id=56)
        self.assertEqual(r4.id, 56)

        r5 = Square(1, 1, id="monaco")
        self.assertEqual(r5.id, "monaco")

    def test_TypeErrors(self):
        self.assertRaises(TypeError, Square, 4, "5")
        self.assertRaises(TypeError, Square, 6, 5, "foo")
        self.assertRaises(TypeError, Square, "6", 5, 10, "faa")

    def test_ValueErrors(self):
        self.assertRaises(ValueError, Square, -4, 7)
        self.assertRaises(ValueError, Square, 6, 7, -1)
        self.assertRaises(ValueError, Square, 0, 6, 0, 1)

    def test_area(self):
        r1 = Square(10, 2)
        self.assertEqual(r1.area(), 100)

        r2 = Square(2, 10)
        self.assertEqual(r2.area(), 4)

        r3 = Square(10, 20, 0, 112)
        self.assertEqual(r3.area(), 100)

        r4 = Square(2, 2, id=56)
        self.assertEqual(r4.area(), 4)

        r5 = Square(1, 1, id="monaco")
        self.assertEqual(r5.area(), 1)

    def test_display(self):
        r1 = Square(1, 2)
        r2 = Square(4, 3)
        r3 = Square(2, 3, 2)
        r4 = Square(3, 2, 1)
        r1_expect_display = '  #\n'
        r2_expect_display = '   ####\n   ####\n   ####\n   ####\n'
        r3_expect_display = '\n\n   ##\n   ##\n'
        r4_expect_display = '\n  ###\n  ###\n  ###\n'
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r1.display()
            self.assertEqual(fake_out.getvalue(), r1_expect_display)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r2.display()
            self.assertEqual(fake_out.getvalue(), r2_expect_display)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r3.display()
            self.assertEqual(fake_out.getvalue(), r3_expect_display)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            r4.display()
            self.assertEqual(fake_out.getvalue(), r4_expect_display)

    def test_print(self):
        r1 = Square(4, 1, 2, 12)
        r1_expect_print = '[Square] (12) 1/2 - 4\n'
        r2 = Square(5, 5, 1)
        r2_expect_print = '[Square] (1) 5/1 - 5\n'
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(r1)
            self.assertEqual(fake_out.getvalue(), r1_expect_print)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(r2)
            self.assertEqual(fake_out.getvalue(), r2_expect_print)

    def test_update(self):
        r1 = Square(10, 10, 10)
        r1.update(89)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(r1)
            self.assertEqual(
                '[Square] (89) 10/10 - 10\n', fake_out.getvalue())
        r1.update(89, 2)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(r1)
            self.assertEqual('[Square] (89) 10/10 - 2\n',
                             fake_out.getvalue())
        r1.update(89, 2, 3)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(r1)
            self.assertEqual('[Square] (89) 3/10 - 2\n',
                             fake_out.getvalue())
        r1.update(89, 2, 4)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(r1)
            self.assertEqual('[Square] (89) 4/10 - 2\n',
                             fake_out.getvalue())
        r1.update(89, 2, 4, 5)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(r1)
            self.assertEqual('[Square] (89) 4/5 - 2\n',
                             fake_out.getvalue())

    def test_update_kwargs(self):
        r1 = Square(10, 10, 10)
        r1.update(size=1, id="sopas")
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(r1)
            self.assertEqual(
                '[Square] (sopas) 10/10 - 1\n', fake_out.getvalue())
        r1.update(y=1, size=2, x=3, id=89)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(r1)
            self.assertEqual('[Square] (89) 3/1 - 2\n',
                             fake_out.getvalue())
        r1.update(x=1, y=3, size=4)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(r1)
            self.assertEqual('[Square] (89) 1/3 - 4\n',
                             fake_out.getvalue())

    def test_dictionary_representation(self):
        r1 = Square(10, 1, 9)
        self.assertEqual(r1.to_dictionary(), {
                         'x': 1, 'y': 9, 'id': 1, 'size': 10})
        r2 = Square(1, 1)
        self.assertEqual(r2.to_dictionary(), {
                         'x': 1, 'y': 0, 'id': 2, 'size': 1})
