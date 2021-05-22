#!/usr/bin/python3
def magic_string():
    magic_string.calls = getattr(magic_string, "calls", -1) + 1
    return "Holberton" + ", Holberton"*magic_string.calls
