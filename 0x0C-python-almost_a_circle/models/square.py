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
        """init function"""
        super().__init__(size, size, x=x, y=y, id=id)

    def __str__(self):
        """str function"""
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x, self.y, self.width)

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """size setter"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """update function"""
        atts = ("id", "size", "x", "y")
        if args != ():
            for (at, val) in zip(atts, args):
                setattr(self, at, val)
            return

        for at, val in kwargs.items():
            if hasattr(self, at):
                setattr(self, at, val)

    def to_dictionary(self):
        """return the dcitionary of the square"""
        return {"x": self.x, "y": self.y, "id": self.id, "size": self.size}
