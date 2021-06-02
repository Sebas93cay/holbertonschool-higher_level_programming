#!/usr/bin/python3
"""
function that returns the list of available attributes and
methods of an object
"""


class MyList(list):
    def print_sorted(self):
        print(sorted(self))
