#!/usr/bin/python3
"""
Module contains from_json_string(my_str)
"""
import json


def from_json_string(my_str):
    """
    Return an object represented by the given json string
    """
    return json.loads(my_str)
