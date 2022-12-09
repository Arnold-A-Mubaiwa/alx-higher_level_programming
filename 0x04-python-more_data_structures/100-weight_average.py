#!/usr/bin/python3

def weight_average(my_list=[]):
    total = 0
    y_total = 0
    if my_list:
        for item in my_list:
            total += (item[0] * item[1])
            y_total += item[1]
        return total / y_total
    else:
        return 0
