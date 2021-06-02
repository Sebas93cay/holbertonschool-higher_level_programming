#!/usr/bin/python3
"""
function that returns the list of available attributes and
methods of an object
"""


class BaseGeometry:
    def area(self):
        raise Exception("area() is not implemented")
