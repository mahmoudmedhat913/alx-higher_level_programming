#!/usr/bin/python3
"""contain function"""


def append_after(filenamr="", search_string="", new_string=""):
    """insert line of text to file"""
    res_line = []
    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            res_line += [line]
            if line.find(search_string) != -1:
                res_line += [new_string]

    with open(filename, 'w', encoding="utf-8") as f:
        f.write("".join(res_line))
