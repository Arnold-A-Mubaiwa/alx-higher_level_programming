#!/usr/bin/python3

def roman_to_int(roman_string):
    rn_2 = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    val = 0
    temp = 0
    if type(roman_string) == str or roman_string is not None:
        for i in roman_string:
            for k, v in rn_2.items():
                if k == i:
                    if v < temp:
                        val += v
                        temp = v
                    elif v == temp:
                        val -= temp
                        val += (v + temp)
                        temp = v
                    elif v > temp:
                        val -= temp
                        val += (v - temp)
                        temp = v
        return val
    elif roman_string is None or type(roman_string) != str:
        return 0
