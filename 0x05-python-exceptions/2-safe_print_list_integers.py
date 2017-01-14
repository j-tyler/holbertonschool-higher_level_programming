#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    c = 0
    for i in my_list:
        try:
            print("{:d}".format(i), end="")
            c = c + 1
            if c == x:
                break
        except (ValueError, TypeError):
            continue
    print()
    return c
