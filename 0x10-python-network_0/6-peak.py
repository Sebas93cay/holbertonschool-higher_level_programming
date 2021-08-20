#!/usr/bin/python3
"""
This module has a function to find a peak in a list of unsortered numbers
"""


def find_peak(list_of_integers):
    """
    return a peak of a list of unsortered numbers
    """
    if list_of_integers is None or list_of_integers == []:
        return None
    length = len(list_of_integers)
    mid = int(length/2)
    peak_comp = is_peak(list_of_integers, mid)
    if peak_comp is 0:
        return list_of_integers[mid]
    elif peak_comp is 1:
        return find_peak(list_of_integers[(mid + 1):])
    return find_peak(list_of_integers[:mid])


def is_peak(n_list, index):
    """
    Return 0 if number from n_list in index index is a peak
    return 1 if next number is bigger than the number in index
    if not return -1 if previous number is bigger
    if a number next to the number in index is equal, the comparison
    is done with the next number
    """
    for direc in [1, -1]:
        dist = 1
        try:
            while (n_list[index] == n_list[index + dist * direc]):
                dist += 1
            if (n_list[index + dist * direc] > n_list[index]):
                return direc
        except IndexError:
            pass
    return 0
