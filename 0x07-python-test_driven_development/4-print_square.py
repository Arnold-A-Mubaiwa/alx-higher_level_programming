#!/usr/bin/python3
"""Define the function print_square"""


def print_square(size):
    """Returns nothing- only prints
    Raises:
        TypeError if size is not int

        ValueError if size is less than 0
    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#",end="")
        print()
