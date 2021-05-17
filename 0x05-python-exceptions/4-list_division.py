#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    i = 0
    list_r = []
    while i < list_length:
        try:
            r = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            r = 0
        except TypeError:
            print("wrong type")
            r = 0
        except IndexError:
            print("out of range")
            r = 0
        finally:
            list_r.append(r)
        i += 1
    return list_r
