#!/usr/bin/python3
def safe_function(fct, *args):
    import sys

    try:
        ret = fct(*args)
    except Exception as er:
        sys.stderr.write("Exception: " + er.args[0] + "\n")
        ret = None
    return ret
