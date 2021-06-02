#!/usr/bin/python3o

"""this module has a function to appends text to a file"""


def append_write(filename="", text=""):
    """
    appends text to filename
    """
    with open(filename, mode="a", encoding="utf-8") as file:
        file.write(text)

    return len(text)
