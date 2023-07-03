#!/usr/bin/python3
"""Rectangle class."""


class Rectangle:
    """Defines an rectangle class"""
    
    def __init__(self, width=0, height=0):
        """Set a private instance attributes"""
        self.__width = width
        self.__height = height
    
    def width(self):
        """Retrive the width"""
        return self.__width

    def width(self, value):
        """Set a value to the width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")
        
        self.__width = value

    def height(self):
        """Retrive the height"""
        return self.__height

    def height(self, value):
        """Set a value to the height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")
        
        self.__height = value
