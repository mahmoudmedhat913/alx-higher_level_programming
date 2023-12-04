#!/usr/bin/python3
"""contain class"""


class MyInt(int):
    """integer class"""
    def __new__(cls, *args, **kwargs):
        """create instance"""
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        """__eq__"""
        return int(self) != other

    def __ne__(self, other):
        """__ne__"""
        return int(self) == other
