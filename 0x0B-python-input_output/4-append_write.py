#!/usr/bin/python3
"""
Module contains append_write(filename="", text="")
"""


def append_write(filename="", text=""):
    """
    Append text to filename
    """
    with open(filename, encoding='utf-8', mode='a') as f:
        return f.write(text)
