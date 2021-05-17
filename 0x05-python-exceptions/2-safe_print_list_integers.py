def safe_print_list_integers(my_list=[], x=0):
    i = 0
    printed = 0
    while i < x:
        try:
            print("{:d}".format(my_list[i]), end="")
            printed = printed + 1
        except (ValueError, TypeError):
            pass
        i = i + 1
    print("")
    return printed
