#!/usr/bin/python3
"""This module has the base class for every other class"""
import csv
import json
import turtle


class Base:
    """Base Class for every other geometry class
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
