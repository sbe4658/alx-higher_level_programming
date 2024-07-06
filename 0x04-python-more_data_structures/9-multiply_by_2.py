#!/usr/bin/python3
def multiply_by_2(a_dict):
    new_dict = {}
    for key in a_dict:
        new_dict.update({key: a_dict.get(key) * 2})
    return new_dict
