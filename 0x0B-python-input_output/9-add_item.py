#!/usr/bin/python3
"""
Add items to list
"""
save_obj = __import__('7-save_to_json_file').save_to_json_file
creat_obj = __import__('8-load_from_json_file').load_from_json_file
import sys

try:
    l = creat_obj("add_item.json")
except FileNotFoundError:
    l = []
for i in range(1, len(sys.argv)):
    l.append(sys.argv[i])

save_obj(l, "add_item.json")
