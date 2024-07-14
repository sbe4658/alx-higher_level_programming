#!/usr/bin/python3
def complex_delete(a_dict, value):
    res = a_dict.copy()
    for key in a_dict:
        if a_dict.get(key) is value:
            res.pop(key)
    return res
