#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):

    tuples = [tuple_a, tuple_b]
    lists = [[], []]
    for i in range(2):
        counter = 0
        for w in tuples[i]:
            lists[i].append(w)
            counter += 1
        if counter < 2:
            for extra in range(counter, 2):
                lists[i].append(0)

    return (lists[0][0] + lists[1][0], lists[0][1] + lists[1][1])
