#!/usr/bin/python3
"""Create BaseGeometry class"""


class BaseGeometry:
    """This class is a representation of a undefined BaseGeometry"""

    def area(self):
        """This function has not been implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """This function check for a int parameter
        Args:
            name (str): name of the parameter
            value (int): parameter to validate
        Raises:
            TypeError if value not is an integer"
        """
        if not type(value) == int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
