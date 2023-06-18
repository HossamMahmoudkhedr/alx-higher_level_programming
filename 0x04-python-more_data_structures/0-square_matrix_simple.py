#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newMatrix = []
    length = 0
    for row in matrix:
        newMatrix.append([])
        for i in row:
            newMatrix[length].append(i * i)
        length += 1
    return newMatrix
