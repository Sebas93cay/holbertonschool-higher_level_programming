#!/usr/bin/python3
"""Square 4 class"""


class Square:
    """Square class"""

    def __init__(self, size=0, position=(0, 0)):
        """Init the square"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """return the square's size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """set the square's size"""
        if (isinstance(value, int) is False):
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self, value):
        """return position property"""
        return self.__position

    @position.setter
    def position(self, value):
        """set the __position"""
        if not (isinstance(value, tuple) and
                len(value) == 2 and
                all(isinstance(v, int) for v in value) and
                all(v >= 0 for v in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """return the square's area"""
        return (self.__size ** 2)

    def my_print(self):
        """print the square to stdout"""
        if self.__size != 0:
            for row in range(self.__position[1]):
                print("")
            for col in range(self.__size):
                print("{}{}".format(" " * self.__position[0],
                                    "#" * self.__size))
        else:
            print("")
