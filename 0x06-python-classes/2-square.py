#!/usr/bin/python3

"""Define a class square"""


class Square:
    """Represent a square"""

    def __init__(self, size=0):
        """Initialize a square

        Args:
            size (int): the size of the square
        """
        try:
            self.__size = size
        except TypeError:
            raise print("size must be an integer")
        except ValueError:
            raise print("size must be >= 0")
