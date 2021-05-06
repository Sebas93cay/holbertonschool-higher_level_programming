#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dictionary = {}
    if a_dictionary is None:
        return None
    for k in a_dictionary.keys():
        new_dictionary[k] = a_dictionary[k]*2
    return new_dictionary
