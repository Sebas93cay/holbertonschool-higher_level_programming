#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys

    printed = True
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError) as er:
        sys.stderr.write("Exception: " + er.args[0] + "\n")
        printed = False
    return printed
