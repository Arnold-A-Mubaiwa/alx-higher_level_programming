#!/usr/bin/python3
"""
Creating Square class 
"""

class Square:
    """
    class Square consructor
    """
    def __init__(self, size=0):
        """
        __size is private
        """
        try:
            int(size)
            if size >= 0:
                self.__size = size
            else:
                raise ValueError('size must be >= 0')
        except TypeError:
            print("size must be an integer")
