#!/usr/bin/python3
"""module contain function"""


def is_same_class(obj, a_class):
        """return True if object is exactly an instance of specified class, otherwise false"""
        return (type(obj) == a_class)
