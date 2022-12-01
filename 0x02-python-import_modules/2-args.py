#!/usr/bin/python3
from sys import argv

num_of_args = len(argv)
print(num_of_args)

if num_of_args <= 1:
    print("0 arguments .")
else:
    for i in range(num_of_args):
        print("{}: {}".format(i, argv[i]))
