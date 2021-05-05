#!/usr/bin/python3
def no_c(my_string):
    new_string = my_string[:]
    for c in my_string:
        if (c is 'c' or c is 'C'):
            idx = new_string.index(c)
            new_string = new_string[:idx]+new_string[idx + 1:]
    return new_string
