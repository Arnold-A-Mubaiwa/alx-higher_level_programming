#!/usr/bin/python3

class Square:

    def __init__(self, size=0, position=(0,0)):
        self.size = size
        self.position = position

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
    
    @property
    def position(self):
        return self.__position
    
    @position.setter
    def position(self, value):
        try:
            int(value[0])
            int(value[1])
            self.__position = value
        except TypeError:
            raise TypeError("position must be a tuple of 2 positive integers")

    def my_print(self):
        space = ""
        if self.__position[1] > 0:
            pass
        else:
            for i in range(self.__position[0]):
                space = space + " "
        if self.size == 0:
            print()
        else:
            for i in range(self.size):
                print(space, end='')
                for j in range(self.size):
                    print("#", end="")
                print()

my_square_1 = Square(3)
my_square_1.my_print()

print("--")

my_square_2 = Square(3, (1, 1))
my_square_2.my_print()

print("--")

my_square_3 = Square(3, (3, 0))
my_square_3.my_print()

print("--")