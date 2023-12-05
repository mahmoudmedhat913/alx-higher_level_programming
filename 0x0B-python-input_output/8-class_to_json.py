#!/usr/bin/python3
"""contain function"""


def class_to_json(obj):
    """return dictionary discribtion with simple data structure"""
    return obj.__dict__
