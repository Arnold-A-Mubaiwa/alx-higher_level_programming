#!/usr/bin/python3

def best_socre(a_dictionary):
    best = None
    if a_dictionary is not 0:
        for key, value in a_dictionary.items():
            if key.index() == 0:
                best = value
            else:
                if value > best:
                    best = value
    else:
        return None
    return best
