#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    the_keys = a_dictionary.keys()
    print(the_keys)
    the_keys = sorted(the_keys)
    for k in the_keys:
        print("{:s}: {}".format(k, a_dictionary[k]))
