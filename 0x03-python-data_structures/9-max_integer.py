#!/usr/bin/python3

def max_integer(my_list=[]):
    largest = None
    for i in my_list:
        if len(my_list) == 0:
            return largest
        elif my_list.index(i) == 0:
            largest = i
        else:
            if i > largest:
                largest = i
    return largest
