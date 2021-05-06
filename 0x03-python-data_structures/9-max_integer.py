#!/usr/bin/python3
def max_integer(hola=[]):
    print(hola)
    if (hola is None):
        return None
    if (len(hola) == 0):
        return None
    max = hola[0]
    for i in hola:
        if i > max:
            max = i
    return max
