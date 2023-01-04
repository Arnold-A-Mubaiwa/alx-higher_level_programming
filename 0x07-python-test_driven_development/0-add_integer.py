#!/usr/bin/python3
"""Defining a function add_integer"""

def add_integer(a, b=98):
    """Return the sum of two integers a + b
    raises type error if the arguments a or b
    are not integers or floats
    """

    if type(a) != int or type(a) != float:
        raise TypeError("a must be an integer")

    if type(b) != int or type(b) != float:
        raise TypeError("b must be an integer")

    return a + b
