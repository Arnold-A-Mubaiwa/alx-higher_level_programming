#!/usr/bin/python3

def uppercase(str):
    for letter in str:
        p = ord(letter)
        u = p - 32
        print("{}".format(chr(u) if (p > 96 and p < 123) else chr(p)), end='')
    print("")
