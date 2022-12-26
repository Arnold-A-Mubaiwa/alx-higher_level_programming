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

my_square = Square(89)
print("Area: {} for size: {}".format(my_square.area(), my_square.size))

my_square.size = 3
print("Area: {} for size: {}".format(my_square.area(), my_square.size))

try:
    my_square.size = "5 feet"
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))
except Exception as e:
    print(e)