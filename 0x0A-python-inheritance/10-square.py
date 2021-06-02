#!/usr/bin/python3
"""Create Square Class"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Create Square Class, it inherits from rectangle class"""

    def __init__(self, size):
        super().__init__(size, size)
        self.__size = size
