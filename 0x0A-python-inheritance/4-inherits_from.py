#!/usr/bin/python3
"""contain function"""


def inherits_from(obj, a_class):
    """true if obj is subclass"""
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
