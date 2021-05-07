#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list is None or len(my_list) is 0:
        return 0
    sum_up = sum([a*b for a, b in my_list])
    sum_down = sum([b for a, b in my_list])
    return (sum_up/sum_down)
