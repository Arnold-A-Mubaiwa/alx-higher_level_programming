#!/usr/bin/python3

def best_socre(a_dictionary):
    best = None
    if len(a_dictionary) != 0 or a_dictionary != None:
        for  val in a_dictionary.values():
            if best == None:
                best = val
            else:
                if val > best:
                    best = val
    else:
        return best
    return best
