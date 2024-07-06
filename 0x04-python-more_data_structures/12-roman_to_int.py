#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_num = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    res = a = b = 0
    lenght = len(roman_string)
    for idx in range(lenght):
        a = roman_num.get(roman_string[idx])
        if idx + 1 < lenght:
            b = roman_num.get(roman_string[idx + 1])
        if a >= b:
            res += a
        elif a < b:
            res -= a
    return res
