#!/usr/bin/python3

def multiple_returns(sentence):
    first_char = ''
    length = len(sentence)
    if length == 0:
        first_char = None
    else:
        first_char = sentence[0]
    tup = length, first_char
    return tup

print(multiple_returns(''))
