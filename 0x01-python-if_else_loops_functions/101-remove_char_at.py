#!/usr/bin/python3

def remove_char_at(str, n):
    new_str = ''
    for index in range(len(str)):
        if index == n:
            continue
        new_str += "{0}".format(str[index])
    return new_str
