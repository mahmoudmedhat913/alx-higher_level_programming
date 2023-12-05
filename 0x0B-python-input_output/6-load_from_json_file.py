#!/usr/bin/python3
"""contain function"""
import json


def load_from_json_file(filename):
    """create object"""
    with open(filename, "r") as f:
        return json.load(f)
