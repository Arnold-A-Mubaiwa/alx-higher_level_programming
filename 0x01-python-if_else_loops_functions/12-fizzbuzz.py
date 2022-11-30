#!/usr/bin/python3

def fizzbuzz():
    toprint = ''
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            toprint = "FizzBuzz"
        elif num % 3 == 0:
            toprint = "Fizz"
        elif num % 5 == 0:
            toprint = "Buzz"
        else:
            toprint = num
        print("{0}".format(toprint), end=" ")
