#!/usr/bin/python3
"""
Module contains append_after(filename="", search_string="", new_string="")
"""


def append_after(filename="", search_string="", new_string=""):
    """
    appends new_string after any string containing search_string
    """
    with open(filename, encoding='utf-8', mode='r') as f:
        contents = f.readlines()
        flag = 0
        for i, line in enumerate(contents):
            if flag == 1:
                flag = 0
                continue
            if line.find(search_string) != -1:
                contents.insert(i + 1, new_string)
                flag = 1

    with open(filename, encoding='utf-8', mode='w') as f:
        f.write("".join(contents))
