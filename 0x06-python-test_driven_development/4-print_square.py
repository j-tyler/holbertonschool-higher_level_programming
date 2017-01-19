#!/usr/bin/python3
"""
This module prints out a poundsymbol square
There is one function, print_square(size)

>>> print_square(3)
###
###
###
"""


def print_square(size):
    """
    prints out a square with pound symbols
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    s = '#' * size + '\n'
    s = s * size
    print("{:s}".format(s), end="")
