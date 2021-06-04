#!/usr/bin/python3
"""
This module has the base class for every other class
"""


class Base:
    """Base Class for every other class"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
