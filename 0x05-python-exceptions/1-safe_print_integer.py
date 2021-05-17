#!/usr/bin/python3
def safe_print_integer(value):
    if value is None:
        return False
    ret = True
    try:
        print("{:d}".format(value))
    except:
        ret = False
    return ret
