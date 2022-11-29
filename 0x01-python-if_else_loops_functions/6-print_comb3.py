#!/usr/bin/python3
for i in range(10):
    for x in range(i+1, 10):
        if i == 8 and x == 9:
            print("{0}{1}".format(i, x))
            continue
        print("{0}{1}".format(i, x), end=", ")
