#!/usr/bin/python3

"""this module has a function to read from a file"""


def read_file(filename=""):
    """
    Read filename and prints it to stdout
    """
    with open(filename, mode="r", encoding="utf-8") as file:
        print(file.read())
