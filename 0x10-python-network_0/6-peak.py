#!/usr/bin/python3
"""module that find a peak"""


def find_peak(list_of_integers):
    """function that find a peak"""
    list_ = list_of_integers
    if list_ == []:
        return None
    length = len(list_)
    start, end = 0, length - 1
    while start < end:
        mid = start + (end - start)
        if list_[mid] > list_[mid - 1] and list_[mid] > list_[mid + 1]:
            return list_[mid]
        if list_[mid - 1] > list_[mid + 1]:
            end = mid
        else:
            start = mid + 1
    return list_[start]
