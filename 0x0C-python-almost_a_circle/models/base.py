#!/usr/bin/python3
"""
This module has the base class for every other class
"""
import csv
import json
import turtle


class Base:
    """
    Base Class for every other geometry class
    Args:
        id
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """init function"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns a json string of a list of dictionaries"""
        if list_dictionaries is None:
            return "[]"
        jsons = "["
        for i, d in enumerate(list_dictionaries):
            if i != 0:
                jsons += ", "
            jsons += json.dumps(d)
        jsons += "]"
        return jsons

    @classmethod
    def save_to_file(cls, list_objs):
        """Save boject as a json string in a file named <Nameclass>.json"""
        f_name = cls.__name__ + ".json"
        d_list = [ob.to_dictionary() for ob in list_objs]
        json_s = Base.to_json_string(d_list)
        with open(f_name, mode="w", encoding="utf-8") as file:
            file.write(json_s)

    def from_json_string(json_string):
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Create a new object with attributes from dictionary"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            return

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Create a list of instances from a list of dictionaries in a file"""
        f_name = cls.__name__ + ".json"
        try:
            with open(f_name, mode="r", encoding="utf-8") as file:
                content = file.read()
        except:
            return []

        dics = json.loads(content)
        objs = [cls.create(**d) for d in dics]

        return objs

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """save object in list_objs to a cvs file"""
        file_name = cls.__name__ + ".cvs"

        if cls.__name__ == "Rectangle":
            atts = ("id", "width", "height", "x", "y")
        elif cls.__name__ == "Square":
            atts = ("id", "size", "x", "y")

        with open(file_name, mode="w", encoding="utf-8") as file:
            spamwriter = csv.writer(file)
            for obj in list_objs:
                spamwriter.writerow([getattr(obj, att) for att in atts])

    @classmethod
    def load_from_file_csv(cls):
        """loads from cvs file to a list of objects"""
        file_name = cls.__name__ + ".cvs"

        if cls.__name__ == "Rectangle":
            atts = ("id", "width", "height", "x", "y")
        elif cls.__name__ == "Square":
            atts = ("id", "size", "x", "y")

        objs = []
        with open(file_name, newline="") as file:
            spamreader = csv.reader(file)
            for row in spamreader:
                el_dic = {}
                for key, val in zip(atts, row):
                    el_dic[key] = int(val)
                objs.append(cls.create(**el_dic))
        return objs

    @staticmethod
    def draw(list_rectangles, list_squares):
        """draw list of rectangles and squares"""
        Juan = turtle.Turtle()
        turtle.setworldcoordinates(0, -1000, 1000, 0)
        # turtle.setworldcoordinates(0, -1000, 100, 0)
        # turtle.screensize(100, 1000)

        def draw_lists(list, border_color, fill_color, turtle):
            """draw list of objects"""
            turtle.color(border_color, fill_color)
            for rec in list:
                turtle.penup()
                turtle.goto(rec.x, -(rec.y))
                turtle.pendown()
                turtle.begin_fill()
                for i in range(2):
                    if hasattr(rec, "size"):
                        turtle.forward(rec.size)
                    else:
                        turtle.forward(rec.width)
                    turtle.right(90)
                    if hasattr(rec, "size"):
                        turtle.forward(rec.size)
                    else:
                        turtle.forward(rec.height)
                    turtle.right(90)
                turtle.end_fill()

        draw_lists(list_rectangles, "brown", "red", Juan)
        draw_lists(list_squares, "brown", "blue", Juan)
        turtle.done()
