#!/usr/bin/python3o
"""
this module has a function that
returns the JSON representation of an object
"""
import json


def to_json_string(my_obj):
    """
    returns the JSON representation of an object
    """
    return json.dumps(my_obj, sort_keys=True)
