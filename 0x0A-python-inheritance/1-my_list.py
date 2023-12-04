#!/usr/bin/python3
"""contain class"""


class MyList(list):
    """class list"""
    def __init__(self):
        """initialize"""
        super().__init__()

    def print_sorted(self):
        """print list"""
        print(sorted(self))
