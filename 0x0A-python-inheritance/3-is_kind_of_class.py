#!/usr/bin/python3
"""check if obj is from or has inherited from a_class"""


def is_kind_of_class(obj, a_class):
    """check if obj is from or has inherited from a_class"""
    return isinstance(obj, a_class) or issubclass(type(obj), a_class)
