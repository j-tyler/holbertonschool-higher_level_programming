#!/usr/bin/python3
"""
class MyList testing inheritance
"""


class MyList(list):
    """
    duplicate list method of sorting
    """
    def print_sorted(self):
        print("{}".format(sorted(self)))
