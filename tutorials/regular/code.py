#!/usr/bin/python3
# These codes work perfectly, just that million ways to kill a cat
def uppercase(str):
    for letter in str:
        pos = ord(letter)
        if pos > 96 and pos < 123:
            print("{0}".format(chr(pos - 32)), end='')
        else:
            print("{0}".format(chr(pos)), end='')
