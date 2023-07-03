#!/usr/bin/python3
"""Rectangle class."""


class Rectangle:
    """Defines an rectangle class"""


    number_of_instances = 0

    def __init__(self, width=0, height=0, print_symbol="#"):
        """Set a private instance attributes
        Args:
            width (int): the width of the rectangle
            height (int): the height of the rectangle
        """
        Rectangle.number_of_instances += 1
        self.width = width
        self.height = height
        self.print_symbol = print_symbol

    @property
    def width(self):
        """Retrive the width"""
        return self.__width

    @width.setter
    def width(self, value):
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
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return (self.__width * self.__height)

    def perimeter(self):
        if self.__height == 0 or self.width == 0:
            return 0
        return (2 * (self.__width + self.__height))

    def __str__(self):
        rectangle = ""
        if self.__width != 0 and self.__height != 0:
            for i in range(self.__height):
                rectangle += str(self.print_symbol) * self.__width + "\n"
        return rectangle

    def __repr__(self):
        return ("Rectangle({:d}, {:d})".format(self.__width, self.__height))

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
