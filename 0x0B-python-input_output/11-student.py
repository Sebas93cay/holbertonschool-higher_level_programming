#!/usr/bin/python3
"""
this module has a function that
has a student class
"""


class Student:
    """
    student class
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if type(attrs) == list and \
                all(type(i) == str for i in attrs):
            attributes = {}
            for key in attrs:
                try:
                    attributes[key] = self.__dict__[key]
                except Exception:
                    pass
            return attributes
        return self.__dict__

    def reload_from_json(self, json):
        for att in json.keys():
            self.__dict__[att] = json[att]
