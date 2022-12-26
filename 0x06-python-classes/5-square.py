#!/usr/bin/python3

class Square:

    def __init__(self, size=0):
        self.size = size

    def area(self):
        """
        Calculates the area
        Returns the current square area
        """
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        try:
            int(value)
            if value >= 0:
                self.__size = value
            else:
                raise ValueError('size must be >= 0')
        except (TypeError, ValueError):
                raise TypeError("size must be an integer")
    
    def my_print(self):
        if self.size == 0:
            print()
        else:
            for i in range(self.size):
                for j in range(self.size):
                    print("#", end="")
                print()
