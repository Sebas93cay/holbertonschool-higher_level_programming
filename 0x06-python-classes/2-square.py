#!/usr/bin/python3
"""Square 2 class"""


class Square:
    """Square class"""

    def __init__(self, size_s=0):
        if (isinstance(size_s, int) is False):
            raise TypeError("size must be an integer")
        if (size_s < 0):
            raise ValueError("size must be >= 0")
        self.__size = size_s
