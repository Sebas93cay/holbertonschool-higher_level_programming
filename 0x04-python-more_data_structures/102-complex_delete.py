#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if a_dictionary is None:
        return None
    keys = list(a_dictionary.keys())
    for k in keys:
        if a_dictionary[k] is value:
            a_dictionary.pop(k, None)
    return a_dictionary
