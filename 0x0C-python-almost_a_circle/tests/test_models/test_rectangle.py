#!/usr/bin/python3

from io import StringIO
from models.rectangle import Rectangle, Base
import unittest
from unittest.mock import patch


class testRectangle(unittest.TestCase):
    def setUp(self):
        super().setUp()
        Base._Base__nb_objects = 0

    def test_init(self):
        # test rectangles id's
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 2)

        r3 = Rectangle(10, 2, 0, 0, 112)
        self.assertEqual(r3.id, 112)

        r4 = Rectangle(2, 2, id=56)
        self.assertEqual(r4.id, 56)

        r5 = Rectangle(1, 1, id="monaco")
        self.assertEqual(r5.id, "monaco")

    def test_TypeErrors(self):
        self.assertRaises(TypeError, Rectangle, 4, "5")
        self.assertRaises(TypeError, Rectangle, 6, 5, "foo")
        self.assertRaises(TypeError, Rectangle, 6, 5, 10, "faa")

    def test_ValueErrors(self):
        self.assertRaises(ValueError, Rectangle, -4, 7)
        self.assertRaises(ValueError, Rectangle, 6, 7, 0, -1)
        self.assertRaises(ValueError, Rectangle, 6, 0, 0, 1)

    def test_area(self):
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.area(), 20)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)

        r3 = Rectangle(10, 20, 0, 0, 112)
        self.assertEqual(r3.area(), 200)

        r4 = Rectangle(2, 2, id=56)
        self.assertEqual(r4.area(), 4)

        r5 = Rectangle(1, 1, id="monaco")
        self.assertEqual(r5.area(), 1)

    def test_display(self):
        r1 = Rectangle(1, 2)
        r2 = Rectangle(4, 3)
        r3 = Rectangle(2, 3, 2, 2)
        r4 = Rectangle(3, 2, 1, 0)
        r1_expect_display = '#\n#\n'
        r2_expect_display = '####\n####\n####\n'
        r3_expect_display = '\n\n  ##\n  ##\n  ##\n'
        r4_expect_display = ' ###\n ###\n'
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
        r1 = Rectangle(4, 6, 2, 1, 12)
        r1_expect_print = '[Rectangle] (12) 2/1 - 4/6\n'
        r2 = Rectangle(5, 5, 1)
        r2_expect_print = '[Rectangle] (1) 1/0 - 5/5\n'
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(r1)
            self.assertEqual(fake_out.getvalue(), r1_expect_print)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(r2)
            self.assertEqual(fake_out.getvalue(), r2_expect_print)

    def test_update(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(89)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(r1)
            self.assertEqual(
                '[Rectangle] (89) 10/10 - 10/10\n', fake_out.getvalue())
        r1.update(89, 2)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(r1)
            self.assertEqual('[Rectangle] (89) 10/10 - 2/10\n',
                             fake_out.getvalue())
        r1.update(89, 2, 3)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(r1)
            self.assertEqual('[Rectangle] (89) 10/10 - 2/3\n',
                             fake_out.getvalue())
        r1.update(89, 2, 3, 4)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(r1)
            self.assertEqual('[Rectangle] (89) 4/10 - 2/3\n',
                             fake_out.getvalue())
        r1.update(89, 2, 3, 4, 5)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(r1)
            self.assertEqual('[Rectangle] (89) 4/5 - 2/3\n',
                             fake_out.getvalue())

    def test_update_kwargs(self):
        r1 = Rectangle(10, 10, 10, 10)
        r1.update(height=1, id="sopas")
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(r1)
            self.assertEqual(
                '[Rectangle] (sopas) 10/10 - 10/1\n', fake_out.getvalue())
        r1.update(width=1, x=2)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(r1)
            self.assertEqual(
                '[Rectangle] (sopas) 2/10 - 1/1\n', fake_out.getvalue())
        r1.update(y=1, width=2, x=3, id=89)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(r1)
            self.assertEqual('[Rectangle] (89) 3/1 - 2/1\n',
                             fake_out.getvalue())
        r1.update(x=1, height=2, y=3, width=4)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(r1)
            self.assertEqual('[Rectangle] (89) 1/3 - 4/2\n',
                             fake_out.getvalue())

    def test_dictionary_representation(self):
        r1 = Rectangle(10, 2, 1, 9)
        self.assertEqual(r1.to_dictionary(), {
                         'x': 1, 'y': 9, 'id': 1, 'height': 2, 'width': 10})
        r2 = Rectangle(1, 1)
        self.assertEqual(r2.to_dictionary(), {
                         'x': 0, 'y': 0, 'id': 2, 'height': 1, 'width': 1})
