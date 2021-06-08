#!/usr/bin/python3
"""This module define the Base class"""
import json
import csv
import turtle


class Base:
    """Represent a Geometry Base
    Args:
        nb_objects (int): number of base class instance
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""
        return json.dumps(list_dictionaries) if list_dictionaries else "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file"""
        if not list_objs:
            list_objs = []
        objects = list(map(lambda obj: obj.to_dictionary(), list_objs))
        with open(cls.__name__ + ".json", "w") as f:
            f.write(Base.to_json_string(objects))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string"""
        return json.loads(json_string) if json_string else []

    @classmethod
    def create(cls, **dictionary):
        """Return a new instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            base = cls(1, 1)
        else:
            base = cls(1)
        base.update(**dictionary)
        return base

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances in a json file"""
        try:
            with open(cls.__name__ + ".json", "r") as f:
                list_dicts = cls.from_json_string(f.read())
                return [cls.create(**dic) for dic in list_dicts]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Writes the CSV string representation of list_objs to a file"""
        objects = list(map(lambda obj: obj.to_dictionary(), list_objs))

        if cls.__name__ == "Rectangle":
            keys = ["id", "width", "height", "x", "y"]
        else:
            keys = ["id", "size", "x", "y"]

        with open(cls.__name__ + ".csv", "w") as f:
            if len(objects) > 0:
                dict_writer = csv.DictWriter(f, keys)
                dict_writer.writeheader()
                dict_writer.writerows(objects)

    @classmethod
    def load_from_file_csv(cls):
        """Returns a list of instances in a csv file"""
        try:
            with open(cls.__name__ + ".csv", "r") as f:
                l = [
                    {k: int(v) for k, v in row.items()}
                    for row in csv.DictReader(f, skipinitialspace=True)
                ]
                return [cls.create(**dic) for dic in l]
        except FileNotFoundError:
            return []

    def draw(list_rectangles, list_squares):
        """Open a window and draws all the Rectangles and Squares"""
        t = turtle.Turtle()
        for r in list_rectangles:
            for _ in range(4):
                if _ % 2 == 0:
                    t.forward(20)  # Forward turtle by l units
                    t.left(90)  # Turn turtle by 90 degree
                else:
                    t.forward(20)  # Forward turtle by w units
                    t.left(90)  # Turn turtle by 90 degree
