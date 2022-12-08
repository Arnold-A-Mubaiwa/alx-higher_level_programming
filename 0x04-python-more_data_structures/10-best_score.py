#!/usr/bin/python3

def best_score(a_dictionary):
    best = None
    best_mark = None
    if a_dictionary is not None:
        for key, val in a_dictionary.items():
            if best is None and best_mark is None:
                best = key
                best_mark = val
            else:
                if val > best_mark:
                    best = key
                    best_mark = val
    else:
        return best
    return best
