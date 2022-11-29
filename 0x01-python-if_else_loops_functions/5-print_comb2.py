#!/usr/bin/python3
# for i in range(100):
#     print("{0:02}".format(i), end='')
#     if i != 99:
#         print(", ", end='')

for i in range(100):
    if i == 99:
        print("{0}".format(i))
    else:
        print("{0:02}".format(i), end=', ')
