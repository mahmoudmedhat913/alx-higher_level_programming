#!/usr/bin/python3
"""contain class"""


def add_attribute(obj, attribute, value):
    """add attribute"""
    if '__dict__' not in dir(obj):
        raise TypeError("can't add new attribute")
    if '__slots__' in dir(obj):
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, attribute, value)
