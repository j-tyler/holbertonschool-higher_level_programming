#!/usr/bin/python3
"""
Module contains write_file(filename="", text="")
"""


def write_file(filename="", text=""):
    """
    Write given text to given file
    """
    with open(filename, encoding='utf-8', mode='w') as f:
        return f.write(text)
