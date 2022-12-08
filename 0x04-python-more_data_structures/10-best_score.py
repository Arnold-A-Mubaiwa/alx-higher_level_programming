#!/usr/bin/python3

def best_score(a_dictionary):
    best = None
    best_mark = None
    if a_dictionary != None:
        for  key, val in a_dictionary.items():
            if best == None and best_mark == None:
                best = key
                best_mark = val
            else:
                if val > best_mark:
                    best = key
                    best_mark = val
    else:
        return best
    return best

a_dictionary = {'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}
best_key = best_score(a_dictionary)
print("Best score: {}".format(best_key))

best_key = best_score(None)
print("Best score: {}".format(best_key))