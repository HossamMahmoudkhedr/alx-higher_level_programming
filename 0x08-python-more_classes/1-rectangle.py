#!/usr/bin/python3
"""Rectangle class."""


class Rectangle:
    """Defines an rectangle class
    
    Args:
        width: the width of the rectangle
        height: the height of the rectangle

    Return:
        returns the width and the height

    Raise:
        Raises a ValueError and TypeError
    """
    
    def __init__(self, width=0, height=0):
        """Set a private instance attributes"""
        self.width = width
        self.height = height

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
