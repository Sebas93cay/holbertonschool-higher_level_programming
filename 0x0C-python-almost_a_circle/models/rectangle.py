#!/usr/bin/python3
"""
This module has the rectangle class
"""

from models.base import Base


class Rectangle(Base):
    """Rectangle Class"""
    __nb_objects = 0

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        return self.__width * self.__height

    def display(self):
        print("\n"*self.__y, end='')
        print((' '*self.__x+'#'*self.__width+'\n')*self.__height, end='')

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x, self.y,
                                                       self.__width, self.__height)

    def update(self, *args, **kwargs):
        if args != None and len(args) != 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                elif i == 1:
                    self.width = args[i]
                elif i == 2:
                    self.height = args[i]
                elif i == 3:
                    self.x = args[i]
                elif i == 4:
                    self.y = args[i]
            return

        if (kwargs != {}):
            if 'width' in kwargs.keys():
                self.width = kwargs['width']
            if 'height' in kwargs.keys():
                self.height = kwargs['height']
            if 'x' in kwargs.keys():
                self.x = kwargs['x']
            if 'y' in kwargs.keys():
                self.y = kwargs['y']
            if 'id' in kwargs.keys():
                self.id = kwargs['id']
            return

    def to_dictionary(self):
        return {'x': self.x,
                'y': self.y,
                'id': self.id,
                'width': self.width,
                'height': self.height}
