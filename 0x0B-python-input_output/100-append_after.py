#!/usr/bin/python3
"""
this module has a function that
inserts a line of text to a file, after each
line containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """
    inserts a line of text to a file, after each
    line containing a specific string
    """
    with open(filename, mode="r", encoding="utf-8") as file:
        content = file.readlines()

    i = 0
    while i < len(content):
        if(content[i][len(content[i])-1] != '\n'):
            content[i] += '\n'
        if (content[i].find(search_string) != -1):
            content.insert(i+1, new_string)
            i += 1
        i += 1

    with open(filename, mode="w", encoding="utf-8") as file:
        file.write("".join(content))
