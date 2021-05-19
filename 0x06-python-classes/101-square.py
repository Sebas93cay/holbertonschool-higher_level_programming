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
    def position(self):
        """return position property"""
        return self.__position

    @position.setter
    def position(self, value):
        """set the __position"""
        if (type(value) is not tuple or
            len(value) is not 2 or
            any(map(lambda x: type(x) is not int, value)) or
                any(x < 0 for x in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """return the square's area"""
        return (self.__size ** 2)

    def my_print(self):
        """print the square to stdout"""
        if self.__size is not 0:
            print("\n" * self.__position[1], end='')
            for i in range(self.__size):
                print(" " * self.__position[0], end='')
                print("#" * self.__size)
        else:
            print("")

    def __str__(self):
        """str to convert square to str"""
        text = ""
        if self.__size is not 0:
            text = text+"\n" * self.__position[1]
            for i in range(self.__size - 1):
                text = text + " " * self.__position[0] + \
                    "#" * self.__size+"\n"
            text = text + " " * self.__position[0] + \
                "#" * self.__size
        return text
