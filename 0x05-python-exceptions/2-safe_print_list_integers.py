def safe_print_list_integers(my_list=[], x=0):
    i = 0
    while i < x:
        try:
            print("{:d}".format(my_list[i]))
        except ValueError:
            pass
        i = i + 1
    return i
