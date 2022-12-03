#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for j in range(len(i)):
            v = " "
            if len(i) - 1 == j:
                v = ''
            print("{:d}".format(i[j]), end=v)
        print()
