#!/usr/bin/python3
"""
List inherited from list
"""


class MyList(list):
    """List inherited from list with sorted method for print"""

    def print_sorted(self):
        print(sorted(self))
