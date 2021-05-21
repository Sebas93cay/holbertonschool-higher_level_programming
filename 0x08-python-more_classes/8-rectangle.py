#!/usr/bin/python3
"""Rectangle Class"""


class Rectangle:
    """Rectangle class"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        Rectangle.number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if (type(value) is not int):
            raise TypeError("width must be an integer")
        if (value < 0):
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if (type(value) is not int):
            raise TypeError("height must be an integer")
        if (value < 0):
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if (self.__width == 0 or self.__height == 0):
            return 0
        return (2*self.__width + 2*self.__height)

    def __str__(self):
        if (self.__width == 0 or self.__height == 0):
            return ""
        text = ((str(self.print_symbol)*self.__width)+"\n") * self.__height
        text = text[:-1]
        return text

    def __repr__(self):
        return "Rectangle("+str(self.__width)+", " +\
            str(self.__height)+")"

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if (rect_1 is None or rect_2 is None):
            return None
        if type(rect_1) is not Rectangle:
            TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            TypeError("rect_2 must be an instance of Rectangle")
        a2 = rect_2.area()
        a1 = rect_1.area()
        if (a2 > a1):
            return rect_2
        return rect_1
