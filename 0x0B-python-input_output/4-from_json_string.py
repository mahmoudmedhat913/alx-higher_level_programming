#!/usr/bin/python3
"""contain function"""
import json


def from_json_string(my_str):
    """return object represented by json"""
    data = json.loads(my_str)
    return data
