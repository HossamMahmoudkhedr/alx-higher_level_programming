#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newMatrix = []
    l = 0
    for row in matrix:
        newMatrix.append([])
        for i in row:
            newMatrix[l].append(i * i)
        l += 1
    
    return newMatrix
