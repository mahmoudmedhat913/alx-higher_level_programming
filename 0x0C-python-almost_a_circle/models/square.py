#!/usr/bin/python3
"""module class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """initialization"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """return string info"""
        return '[{}] ({}) {}/{} - {}'.\
            format(type(self).__name__, self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """size of square"""
        return self.width

    @size.setter
    def size(self, value):
        """size"""
        self.width = value
        self.height = value

    def __update(self, id=None, size=None, x=None, y=None):
        """update instance via */**args"""
        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        """update instance via no keyword and keyword args"""
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)

    def to_dictionary(self):
        """return dictionary representation"""
        return {"id": self.id, "size": self.width,
                "x": self.x, "y": self.y}
