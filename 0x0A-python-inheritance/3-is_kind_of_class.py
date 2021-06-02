#!/usr/bin/python3
"""
function that returns the list of available attributes and
methods of an object
"""


def is_kind_of_class(obj, a_class):
    return isinstance(obj, a_class) or issubclass(type(obj), a_class)
