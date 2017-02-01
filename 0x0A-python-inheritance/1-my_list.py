#!/usr/bin/python3
"""
class MyList testing inheritance
"""


class MyList(list):
    """
    duplicate list method of sorting
    """
    def print_sorted(self):
        """
        print the list sorted
        """
        print("{}".format(sorted(self)))
