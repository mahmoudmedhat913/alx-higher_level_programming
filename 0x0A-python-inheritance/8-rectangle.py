#!/usr/bin/python3
"""contain class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle:
    """rectangle class"""
    def __init__(self, width, height):
        """rectangle fuction"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
