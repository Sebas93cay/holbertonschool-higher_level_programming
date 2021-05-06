#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) is 0:
        return None
    best = next(iter(a_dictionary))
    max = a_dictionary[best]
    for k in a_dictionary.keys():
        if a_dictionary[k] > max:
            max = a_dictionary[k]
            best = k
    return best
