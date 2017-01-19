#!/usr/bin/python3
"""
This module prints out a string repeating the name given
There is one function, say_my_name(first_name, last_name="")

>>> say_my_name("Tina", "Lee")
My name is Tina Lee
"""


def say_my_name(first_name, last_name=""):
    """
    prints out a string repeating the given name
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
