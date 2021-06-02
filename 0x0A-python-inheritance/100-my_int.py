#!/usr/bin/python3
"""
MyInt method
"""


class MyInt(int):
    """MyInt methods inherit from int class, but == and !=
    operators are inverted"""

    def __eq__(self, other):
        return 0 != (self - other)

    def __ne__(self, other):
        return 0 == (self - other)
