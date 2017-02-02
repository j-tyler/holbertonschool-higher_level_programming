#!/usr/bin/python3
"""
Module that prints out number of lines in a file
"""


def number_of_lines(filename=""):
    """
    prints out number of lines in file
    """
    f = open(filename, 'r')
    for index, line in enumerate(f):
        pass
    return index + 1
