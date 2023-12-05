#!/usr/bin/python3
"""contain function"""


def write_file(filename="", text=""):
    """write string to text file"""
    with open(filename, encoding="utf-8", mode="w+") as f:
        return f.write(text)
