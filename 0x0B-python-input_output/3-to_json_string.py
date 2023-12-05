#!/usr/bin/python3
"""contain function"""
import json


def to_json_string(my_obj):
    """return json representation"""
    data = json.dumps(my_obj)
    return data
