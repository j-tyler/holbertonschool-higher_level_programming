#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx <= len(my_list) - 1 and idx >= 0:
        my_list[idx] = element
    return my_list
