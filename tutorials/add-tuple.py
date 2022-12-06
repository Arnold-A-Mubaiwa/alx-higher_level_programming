#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):

    t1 = 0
    t2 = 0
    a = 0
    b = 0
    c = 0
    d = 0

    if len(tuple_a) < 2 or len(tuple_b) < 2:
        pass
    if len(tuple_a) >= 2 or len(tuple_b) >= 2:
        pass
    
    t1 = tuple_a[0] + tuple_b[0]
    t2 = tuple_a[1] + tuple_b[1]
    tup = (t1, t2)
    return tup

print (add_tuple((1,6,7), (2,9,7)))