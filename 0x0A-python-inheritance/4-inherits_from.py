#!/usr/bin/python3
"""
replicate issubclass
"""


def inherits_from(obj, a_class):
    """
    replicate issubclass
    """
    if issubclass(type(obj), a_class):
        if type(obj) != a_class:
            return True
    return False
