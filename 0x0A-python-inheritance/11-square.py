#!/usr/bin/python3
"""Create Square Class"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Square Class, it inherits from rectangle class
    it has str method for print"""

    def __init__(self, size):
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
