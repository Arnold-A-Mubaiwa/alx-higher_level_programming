#!/usr/bin/python3

def no_c(mystring):
    newstring = ''
    for i in mystring:
        if i == 'c' or i == 'C':
            continue
        newstring += i
    return newstring