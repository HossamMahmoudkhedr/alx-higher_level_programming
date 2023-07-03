#!/usr/bin/python3
"""Rectangle class."""


class Rectangle:
    """Defines an rectangle class"""
    
    def __init__(self, width=0, height=0):
        """Set a private instance attributes"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Retrive the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set a value to the width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")
        
        self.__width = value

    @property
    def height(self):
        """Retrive the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set a value to the height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")
        
        self.__height = value


my_rectangle = Rectangle(2, 4)
print(my_rectangle.__dict__)

my_rectangle.width = 10
my_rectangle.height = 3
print(my_rectangle.__dict__)