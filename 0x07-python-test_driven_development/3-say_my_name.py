#!/usr/bin/python3
"""
print a name module
funtion receives name and last name and prints it
"""


def say_my_name(first_name, last_name=""):
    """
    say my name: print a names
    funtion receives name and last name and prints it
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
