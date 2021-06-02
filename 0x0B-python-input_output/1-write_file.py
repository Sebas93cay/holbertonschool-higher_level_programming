#!/usr/bin/python3

"""this module has a function to write text to a file"""


def write_file(filename="", text=""):
    """
    write text to filename
    """
    with open(filename, mode="w", encoding="utf-8") as file:
        file.write(text)

    return len(text)
