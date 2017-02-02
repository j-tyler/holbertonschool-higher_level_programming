#!/usr/bin/python3
"""
Module reads lines from file
"""


def read_lines(filename="", nb_lines=0):
    """
    Read given number of lines from file
    """
    l = []
    with open(filename, "r") as f:
        for index, line in enumerate(f):
            if index < nb_lines or nb_lines == 0:
                l.append(line)
            else:
                break
        print("{}".format("".join(l)), end="")
