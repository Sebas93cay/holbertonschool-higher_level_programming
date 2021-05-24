#!/usr/bin/python3
"""
add two integers module
Functions that converts two numbers into integers
and returns their addition
"""


def add_integer(a, b=98):
    """add two integers"""
    try:
        a = int(a)
    except:
        try:
            a = float(a)
        except:
            raise TypeError("a must be an integer")

    try:
        b = int(b)
    except:
        raise TypeError("b must be an integer")

    return a + b
