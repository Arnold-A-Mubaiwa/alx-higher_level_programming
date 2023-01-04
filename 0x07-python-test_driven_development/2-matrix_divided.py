#!/usr/bin/python3
"""Define a function matrix_divide(matrix, div)"""

def matrix_divide(matrix, div):
    """Returns a new matrix
    
    Matrix must be an integer
    """
    if type(div) != int:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(matrix) != list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    tmp = len(matrix[0])
    for i in matrix:
        if type(i) != list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if len(i) != tmp:
            raise TypeError("Each row of the matrix must have the same size")
        tmp = len(i)
    
    new_list = []
    for l in matrix:
        temp =[]
        for value in l:
            temp.append(value/div)
        new_list.append(temp)
    return new_list
