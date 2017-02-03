#!/usr/bin/python3
"""
Module contains save_to_json_file(my_obj, filename)
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Save a json object to file as a string
    """
    with open(filename, encoding='utf-8', mode='w') as f:
        f.write(json.dumps(my_obj))
