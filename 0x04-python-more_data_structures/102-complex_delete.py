#!/usr/bin/python3
def complex_delete(my_dict, value):
    my_dict = dict({k: v for k, v in my_dict.items() if v != value})
    return my_dict
