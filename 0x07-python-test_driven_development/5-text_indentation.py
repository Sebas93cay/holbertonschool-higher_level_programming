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
        if (letter == '.' or letter == '?' or letter == ':' or letter == '\n'):

            """add offset at the beggining and end of part to print"""
            ini = 0
            endi = 0
            while(text[prev_index + ini] == ' '):
                ini += 1
            while(text[prev_index + ini] != '\n' and letter == '\n' and
                  text[i-endi-1] == ' '):
                endi += 1

            """two different prints if letters is a new line or not"""
            if letter != '\n':
                print(text[prev_index+ini:i+1]+"\n")
            else:
                print(text[prev_index+ini:i-endi])

            """update the previous index"""
            prev_index = i + 1

    """ if last letter is different than . ? or :, add offsets"""
    if (letter != '.' and letter != '?' and letter != ':'):
        ini = 0
        endi = 0
        try:
            while(text[prev_index + ini] == ' '):
                ini += 1
        except IndexError:
            return
        while(text[-endi-1] == ' '):
            endi += 1
        print(text[prev_index + ini:], end='')
