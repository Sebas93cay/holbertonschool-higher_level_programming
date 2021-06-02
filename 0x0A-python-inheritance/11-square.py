#!/usr/bin/python3
"""
function that returns the list of available attributes and
methods of an object
"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    def __init__(self, size):
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
