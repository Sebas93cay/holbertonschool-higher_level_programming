#!/usr/bin/python3
"""magic class to create from its bycodes"""


import math


class MagicClass:
    """magic circle"""

    def __init__(self, radius=0):
        self.__radius = 0
        if (type(radius) is not int and type(radius) is not float):
            raise TypeError("radius must must be a number")
        self.__radius = radius

    def area(self):
        """find area"""
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """find circumference"""
        return (2 * math.pi) * self.__radius
