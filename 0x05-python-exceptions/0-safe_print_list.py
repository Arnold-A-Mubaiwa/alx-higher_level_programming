#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    count = 0          
    list_x = []
    real_number = 0
    to_use = None

    for i in my_list:
        count += 1

    try:
        my_list[x]
        to_use = x
    except IndexError:
        to_use = count

    list_x = my_list[:to_use]
    real_number = to_use
    for i in list_x:
        print(i, end='')
    print()
    return real_number
