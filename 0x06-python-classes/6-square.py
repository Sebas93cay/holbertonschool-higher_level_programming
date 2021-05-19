#!/usr/bin/python3
"""Square 4 class"""


class Square:
    """Square class"""

    def __init__(self, size=0, position=(0, 0)):
        """Init the square"""
        self.__size = size
        good_pos = True
        while (good_pos):
            if type(position) is not tuple:
                good_pos = False
                break
            if len(position) is not 2:
                good_pos = False
                break
            if ((type(position[0]) is not int) or
                    (type(position[1]) is not int)):
                good_pos = False
                break
            if (position[0] < 0 or position[1] < 0):
                good_pos = False
                break
            break
        if good_pos is not True:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def area(self):
        """return the square's area"""
        return self.__size ** 2

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

    def my_print(self):
        """print the square to stdout"""
        if self.__size is not 0:
            for i in range(self.__position[1]):
                print('')
            for i in range(self.__size):
                for w in range(self.__position[0]):
                    print(' ', end='')
                for j in range(self.__size):
                    print("#", end='')
                print('')
        else:
            print('')

    @property
    def position(self, value):
        """return position property"""
        return self.__position

    @position.setter
    def position(self, value):
        """set the __position"""
        good_pos = True
        while (good_pos):
            if type(value) is not tuple:
                good_pos = False
                break
            if len(value) is not 2:
                good_pos = False
                break
            if ((type(value[0]) is not int) or
                    (type(value[1]) is not int)):
                good_pos = False
                break
            if (value[0] < 0 or value[1] < 0):
                good_pos = False
                break
            break
        if good_pos is not True:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
