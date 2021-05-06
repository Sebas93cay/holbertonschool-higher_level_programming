#!/usr/bin/python3
def uniq_add(my_list=[]):
    numbers = []
    for num in my_list:
        if num not in numbers:
            numbers.append(num)
    return (sum(numbers))
