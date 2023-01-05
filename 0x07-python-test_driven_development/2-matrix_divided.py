#!/usr/bin/python3
"""Define a function matrix_divided(matrix, div)"""

def matrix_divided(matrix, div):
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
            result = value/div
            if type(result) == float:
                result = round(result, 2)
            temp.append(result)
        new_list.append(temp)

    return new_list

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(matrix_divided(matrix, 3))
print(matrix)