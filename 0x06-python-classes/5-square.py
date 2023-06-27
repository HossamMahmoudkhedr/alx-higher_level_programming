#!/usr/bin/python3

"""Define a class square"""


class Square:
    """Represent a square"""

    def __init__(self, size=0):
        """Initialize a square

        Args:
            size (int): the size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        for i in range(self.__size):
            for l in range(self.__size):
                print('#', end="")
            print()
        if self.__size == 0:
            print()
