#!/usr/bin/python3
"""
module for function that prints a text with 2 new
lines after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    module for function that prints a text with 2 new
    lines after each of these characters: ., ? and :
    """
    if (type(text) != str):
        raise TypeError("text must be a string")
    prev_index = 0
    for i, letter in enumerate(text):
        if (letter == '.' or letter == '?' or letter == ':'):
            print(text[prev_index:i+1]+"\n")
            prev_index = i + 1

    print(text[prev_index:], end='')
