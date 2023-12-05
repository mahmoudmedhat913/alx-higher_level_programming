#!/usr/bin/python3
"""contain function"""


def append_write(filename="", text=""):
    """append string at the end of text file"""
    with open(filename, mode="a+", encoding="utf-8") as f:
        return f.write(text)
