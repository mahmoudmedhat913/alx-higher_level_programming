#!/usr/bin/python3
"""define locked class"""


class LockedClass:
    """ class locked class"""

    __slots__ = ["first_name"]

    def __init__(self):
        self.first_name = "first_name"
