#!/usr/bin/python3
"""divides all elements of a matrix"""


def matrix_divided(matrix, div):
    """Returns a new matrix
    
    Args:
        matrix: the matrix
        div: the division number
    
    Return:
        new matrix
    
    Raises:
        TypeError: if the number is not a number
    """
    newMatrix = []
    counter = 0
    if not (isinstance(div, int) or isinstance(div, float)):
        raise TypeError("div must be a number")
    
    if div == 0:
        raise ZeroDivisionError("division by zero")
    length = len(matrix[0])
    for i in matrix:
        if len(i) != length:
            raise TypeError("Each row of the matrix must have the same size")
        newMatrix.append([])
        for number in i:
            if not (isinstance(number, int) or isinstance(number, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            else:
                newMatrix[counter].append(round(number/div, 2))
        counter += 1
    
    return newMatrix
