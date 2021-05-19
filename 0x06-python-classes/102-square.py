#!/usr/bin/python3
"""Square 4 class"""


class Square:
    """Square class"""

    def __init__(self, value=0):
        if (isinstance(value, int) is False):
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size ** 2

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if (isinstance(value, int) is False):
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def __lt__(self, other):
        return self.__size < other.__size

    def __le__(self, other):
        return self.__size <= other.__size

    def __eq__(self, other):
        return self.__size == other.__size

    def __ne__(self, other):
        return self.__size != other.__size

    def __ge__(self, other):
        return self.__size >= other.__size

    def __gt__(self, other):
        return self.__size > other.__size
