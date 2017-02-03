#!/usr/bin/python3
"""
Module contains load_from_json_file
"""
import json


def load_from_json_file(filename):
    """
    load a json object from file
    """
    with open(filename, encoding='utf-8', mode='r') as f:
        text = f.read()
        return json.loads(text)
