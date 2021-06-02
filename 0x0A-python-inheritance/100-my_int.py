#!/usr/bin/python3
"""
function that returns the list of available attributes and
methods of an object
"""


class MyInt(int):
    def __eq__(self, other):
        return 0 != (self - other)

    def __ne__(self, other):
        return 0 == (self - other)
