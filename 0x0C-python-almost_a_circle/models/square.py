#!/usr/bin/python3
""" Rectangle class """
from rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(width=size, height=size, x=x, y=y, id=id)
        self.size = size
    def __str__(self):
        return '[Square] ({}) {}/{} - {}'.format(self.id, self.x, self.y,self.size )
