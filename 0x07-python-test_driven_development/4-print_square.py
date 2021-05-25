#!/usr/bin/python3
"""
print a square module
the function prints a square with the character #.
"""


def print_square(size):
    """ prints a square with the character #"""
    if type(size) != int or (type(size) == float and size < 0):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    print(("#"*size+"\n") * size, end='')
