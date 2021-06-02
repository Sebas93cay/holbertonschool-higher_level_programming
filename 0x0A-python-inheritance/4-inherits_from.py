#!/usr/bin/python3
"""
function that returns the list of available attributes and
methods of an object
"""


def inherits_from(obj, a_class):
    a = issubclass(type(obj), a_class)
    b = not type(obj) == a_class
    return a and b
