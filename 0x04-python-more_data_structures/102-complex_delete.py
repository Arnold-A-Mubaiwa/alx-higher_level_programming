#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    list_ = []
    for k, v in a_dictionary.items():
        if v == value:
            list_.append(k)

    for i in list_:
        del a_dictionary[i]
    return a_dictionary
