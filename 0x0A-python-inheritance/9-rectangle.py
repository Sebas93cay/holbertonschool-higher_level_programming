#!/usr/bin/python3
"""
function that returns the list of available attributes and
methods of an object
"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        super().__init__()
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__widht = width
        self.__height = height

    def area(self):
        return self.__height * self.__widht

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__widht, self.__height)
