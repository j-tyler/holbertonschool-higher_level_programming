#!/usr/bin/python3
"""
This module adds two integers.
There is one function, add_integer().

>>> add_integer(4, 5)
9
"""


def add_integer(a, b):
    """
    Returns addition of a and b. Numbers must be valid.
    Floats are truncated to floor.
    """
    if not isinstance(a, (int, float)):
        if not isinstance(b, (int, float)):
            raise TypeError("a must be an integer\nb must be an integer")
        else:
            raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if a == float("inf") or b == float("inf"):
        raise OverflowError("Numbers are approaching infinity")
    return int(a) + int(b)
