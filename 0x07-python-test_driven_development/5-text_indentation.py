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
    for letter in text:
        if letter in list_x:
            print()
        else:
            print(letter, end='')
