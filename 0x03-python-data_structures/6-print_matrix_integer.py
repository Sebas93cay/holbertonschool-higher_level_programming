#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    counter = 0
    for x in matrix:
        last_idx = len(x) - 1
        for y in x:
            print("{:d}".format(y), end=(' ' if counter < last_idx else ''))
            counter += 1
        print('')
        counter = 0
