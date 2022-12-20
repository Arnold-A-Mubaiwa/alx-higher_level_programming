#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    num = 0
    try:
        my_list[x-1]
        my_list = my_list[:x]
        for i in my_list:
            try:
                int(i)
                print("{:d}".format(i), end='')
                num += 1
            except (TypeError, ValueError):
                pass
        print()
    except TypeError:
        pass
    return num
