#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        c = 0
        while c < x:
            print('{:d}'.format(my_list[c]), end="")
            c += 1
    except (IndexError, ValueError):
        print()
        return c
    print()
    return c
