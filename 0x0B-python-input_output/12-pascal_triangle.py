#!/usr/bin/python3
"""contain function"""


def pascal_triangle(n):
    """return list of list of integers"""
    if n <= 0:
        return []
    a = [[] for i in range(n)]
    for i in range(n):
        for j in range(i + 1):
            if j < i:
                if j == 0:
                    a[i].append(1)
                else:
                    a[i].append(a[i - 1][j] + a[i - 1][j - 1])

            elif j == i:
                a[i].append(1)
    return a
