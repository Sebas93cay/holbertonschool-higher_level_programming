#!/usr/bin/python3
"""
This module has the base class for every other class
"""

import json
from json.encoder import JSONEncoder


class Base:
    """Base Class for every other class"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns a json string of a list of dictionaries"""
        if list_dictionaries == None:
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
        f_name = cls.__name__+".json"
        d_list = [ob.to_dictionary() for ob in list_objs]
        json_s = Base.to_json_string(d_list)
        with open(f_name, mode="w", encoding="utf-8") as file:
            file.write(json_s)

    def from_json_string(json_string):
        if json_string == None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Create a new object with attributes from dictionary"""
        if(cls.__name__ == 'Rectangle'):
            dummy = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy = cls(1)
        else:
            return

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Create a list of instances from a list of dictionaries in a file"""
        f_name = cls.__name__+".json"
        try:
            with open(f_name, mode="r", encoding="utf-8") as file:
                content = file.read()
        except:
            return []

        dics = json.loads(content)
        objs = [cls.create(**d) for d in dics]

        return objs
