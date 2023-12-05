#!/usr/bin/python3
"""contain function"""


def read_file(filename=""):
    """read text file UTF8 and print stdout"""
    with open(filename, encoding="utf-8") as f:
        for line in f:
            print(line, end="")
