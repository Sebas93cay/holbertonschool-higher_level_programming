#!/usr/bin/python3
"""
This module has the square class
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    The class Square is a Recthangle with the same width and heigth
    """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x=x, y=y, id=id)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x,
                                                 self.y,
                                                 self.width)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        atts = ('id', 'size', 'x', 'y')
        if args != ():
            for (at, val) in zip(atts, args):
                setattr(self, at, val)
            return

        for at, val in kwargs.items():
            if hasattr(self, at):
                setattr(self, at, val)

    def to_dictionary(self):
        return {'x': self.x,
                'y': self.y,
                'id': self.id,
                'size': self.size}
