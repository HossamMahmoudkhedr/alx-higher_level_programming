#!/usr/bin/python3
""" Rectangle class """
from rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(width=size, height=size, x=x, y=y, id=id)
        self.__size = size

    def __str__(self):
        return '[Square] ({}) {}/{} - {}'.format(self.id, self.x, self.y,self.__size )

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        super().Validation(size, 'width')
        self.__size = size

    def update(self, *args, **kwargs):
        if len(args) == 0:
            for key, val in kwargs.items():
                self.__setattr__(key, val)
        try:
            self.id = args[0]
            self.__size = args[1]
            self.x = args[2]
            self.y = args [3]
        except IndexError:
            pass
