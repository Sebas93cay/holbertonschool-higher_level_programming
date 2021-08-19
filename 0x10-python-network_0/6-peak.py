#!/usr/bin/python3


def find_peak(list_of_integers):
    if list_of_integers is None or list_of_integers == []:
        return None
    length = len(list_of_integers)
    return recursive_find_peak(n_list=list_of_integers, length=length)


def recursive_find_peak(n_list=None, length=0, comparer=None, force=False):
    mid = int(length/2)
    if comparer is not None and comparer > n_list[mid] and not force:
        return None
    if is_
    return mid


def is_peak(n_list, index):
    try:
        if (n_list[index - 1] > n_list[index]):
            return 0
    except IndexError:
        pass
    try:
        if (n_list[index + 1] > n_list[index]):
            return 0
    except IndexError:
        pass
    return 1



