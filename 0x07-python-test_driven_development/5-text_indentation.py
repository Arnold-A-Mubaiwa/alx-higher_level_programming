#!/usr/bin/python3
"""Define the function text_indentation"""


def text_indentation(text):
    """
    Returns nothing

    Prints out each char to the terminal using a loop until
    it reaches the ., ? or :

    Raises:
        TypeError if the argument passed is not an integer
    """
    list_x = ['.', '?', ':']
    str_l = list(text)
    for i in range(len(str_l)):
        if str_l[i] in list_x:
            print(str_l[i])
            print()
            str_l[i + 1] = ''
        else:
            print(str_l[i], end='')
