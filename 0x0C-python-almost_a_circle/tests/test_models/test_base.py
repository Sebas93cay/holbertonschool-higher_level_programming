#!/usr/bin/python3

from models.base import Base
from models.square import Square
from models.rectangle import Rectangle
import unittest
import os


class testBase(unittest.TestCase):
    def setUp(self):
        super().setUp()
        Base._Base__nb_objects = 0

    def test_init(self):
        # test Base.__init__
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

    def test_json_string(self):
        r1 = Square(8)
        d_r1 = r1.to_dictionary()
        d_3 = {'uno': 1, 'dos': 2}
        self.assertEqual(Base.to_json_string(
            [d_r1, d_3]), '[{"x": 0, "y": 0, "id": 1, "size": 8}, {"uno": 1, "dos": 2}]')
        self.assertEqual(Base.to_json_string(None), '[]')

    def test_save_file(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        with open("Rectangle.json", mode="r", encoding="utf-8") as file:
            rectangle_file = file.read()
        test = self.assertEqual(
            rectangle_file, '[{"x": 2, "y": 8, "id": 1, "width": 10, "height": 7}, {"x": 0, "y": 0, "id": 2, "width": 2, "height": 4}]')
        if test == None:
            os.remove("Rectangle.json")

        r3 = Square(9)
        r4 = Square(4, id=78)
        Square.save_to_file([r3, r4])
        with open("Square.json", mode="r", encoding="utf-8") as file:
            square_file = file.read()
        test = self.assertEqual(
            square_file, '[{"x": 0, "y": 0, "id": 3, "size": 9}, {"x": 0, "y": 0, "id": 78, "size": 4}]')
        if test == None:
            os.remove("Square.json")

    def test_string_to_dictionary(self):
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]
        json_list_input = Rectangle.to_json_string(list_input)
        list_output = Rectangle.from_json_string(json_list_input)
        self.assertEqual(list_output, list_input)

        self.assertEqual([], Square.from_json_string(None))

    def test_create(self):
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        self.assertEqual(r1.to_dictionary(), r2.to_dictionary())

    def test_load_from_file(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual([r1.to_dictionary(), r2.to_dictionary()], [
                         list_rectangles_output[0].to_dictionary(), list_rectangles_output[1].to_dictionary()])

    def test_save_csv(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file_csv(list_rectangles_input)

        list_rectangles_output = Rectangle.load_from_file_csv()

        self.assertEqual([ob.to_dictionary() for ob in list_rectangles_input], [
                         ob.to_dictionary() for ob in list_rectangles_output])

        s1 = Square(5)
        s2 = Square(7, 9, 1)
        list_squares_input = [s1, s2]

        Square.save_to_file_csv(list_squares_input)

        self.assertEqual([ob.to_dictionary() for ob in list_rectangles_input], [
            ob.to_dictionary() for ob in list_rectangles_output])

        list_squares_output = Square.load_from_file_csv()

        self.assertEqual([ob.to_dictionary() for ob in list_squares_input], [
            ob.to_dictionary() for ob in list_squares_output])
