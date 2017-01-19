#!/usr/bin/python3
"""
This module formats text adding newlines after . ? and :
There is one function, text_indentation(text)
This function prints the formatted text

>>> text_indentation("hi. friend")
hi.

friend
"""


def text_indentation(text):
    """
    prints text formatted with two newlines after . ? and :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    new = text.split(".")
    new = [line.strip() for line in new]
    new = [(line + '.\n\n') if index + 1 != len(new) else line
           for index, line in enumerate(new)]
    new = ''.join(new)
    new = new.split(":")
    new = [line.strip(' ') for line in new]
    new = [(line + ':\n\n') if index + 1 != len(new) else line
           for index, line in enumerate(new)]
    new = ''.join(new)
    new = new.split("?")
    new = [line.strip(' ') for line in new]
    new = [(line + '?\n\n') if index + 1 != len(new) else line
           for index, line in enumerate(new)]
    new = ''.join(new)
    print("{:s}".format(new), end="")
