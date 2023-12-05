#!/usr/bin/python3
"""contain function"""
import json


def save_to_json_file(my_obj, filename):
    """write object to text file using json"""
    with open(filename, mode="w") as f:
        json.dump(my_obj, f)
