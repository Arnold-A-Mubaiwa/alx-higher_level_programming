#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_list = []
    for list_i in matrix:
        temp = []
        for item in list_i:
            temp.append(item**2)
        new_list.append(temp)
        return new_list
