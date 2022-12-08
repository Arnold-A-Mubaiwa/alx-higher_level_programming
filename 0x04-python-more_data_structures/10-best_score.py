#!/usr/bin/python3

def best_socre(a_dictionary):
    best = None
    if len(a_dictionary) is not 0:
        for key, value in a_dictionary.items():
            if best == None:
                best = value
                key = key
            else:
                if value > best:
                    best = value
    else:
        return best
    return best
