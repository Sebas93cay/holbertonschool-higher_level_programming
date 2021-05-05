#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    ret = []
    for i in my_list:
        ret.append(True if i % 2 == 0 else False)

    return ret
