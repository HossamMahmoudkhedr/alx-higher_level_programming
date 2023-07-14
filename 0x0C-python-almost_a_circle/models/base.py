#!/usr/bin/python3
""" The Base Class """


class Base:
    __nb_objects = 0
    def __init__(self, id=None):
        if id != None:
            self.id = id
        else:
            self.__class__.__nb_objects += 1
            self.id = self.__class__.__nb_objects
