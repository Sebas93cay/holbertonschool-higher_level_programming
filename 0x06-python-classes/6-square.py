#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""6-square
A Square class with size and position as  attributes (and its
getter and setter methods), and area and my_print (prints square with '#'
charater) as methods.
"""


class Square:
    """A simple Square class.

    Attributes:
            __size (int): The size of the square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initialization of Square object with size and position.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """The size of the square.
        For the setter:
        Args:
            value (int): The size of the square.
        Raises:
            TypeError: Size entered must be an integer.
            ValueError: Size entered must be a positive integer.
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """The position from the topmost left part of the screen
        in characters of the square when printed.
        For the setter:
        Args:
            value (:obj:`tuple` of :obj:`int`): (x, y) The coordinates of the
                square from the topmost left part of othe screen in characters.
        Raises:
            TypeError: Position entered must be a tuple of 2 positive integers.
        """
        return self.__position

    @position.setter
    def position(self, value):
        if not (isinstance(value, tuple) and
                len(value) == 2 and
                all(isinstance(v, int) for v in value) and
                all(v >= 0 for v in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculates the area of a square.
        Returns:
            The area of a square.
        """
        return (self.__size ** 2)

    def my_print(self):
        """Prints in stdout the square with the '#' character, and precedes
        them with spaces (self.__position offset (x, y)).
        If self.__size is 0, then it only prints a new line.
        """
        if self.__size != 0:
            for row in range(self.__position[1]):
                print("")
            for col in range(self.__size):
                print("{}{}".format(" " * self.__position[0],
                                    "#" * self.__size))
        else:
            print("")
