#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = 0
    uniq = set(my_list)
    for n in uniq:
        result += n
    return result
