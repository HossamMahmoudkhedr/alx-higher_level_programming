#!/usr/bin/python3
"""This function adds two integers"""


def add_integer(a, b=98):
    """Return the value of adding a and b
    
    Args: 
        a: the first integer
        b: the second integer

    Returns:
        Sum of the two arguments

    Raises:
        TypeError: if the argument is not an integer or float
    """
    if not (isinstance(a, int) or isinstance(a, float)):
        raise TypeError("a must be an integer")
    if not (isinstance(b, int) or isinstance(b, float)):
        raise TypeError('b must be an integer')

    if type(a) == float or type(b) == float:
        a = int(a)
        b = int(b)
    
    return (a + b)
