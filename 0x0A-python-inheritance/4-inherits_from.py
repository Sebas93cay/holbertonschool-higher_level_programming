#!/usr/bin/python3
"""check if obj has inherited from a_class"""


def inherits_from(obj, a_class):
    """check if obj has inherited from a_class"""
    a = issubclass(type(obj), a_class)
    b = not type(obj) == a_class
    return a and b
