#!/usr/bin/python3

def max_integer(my_list=[]):
    if my_list:
        max_num = my_list[0]
        [max_num := item for item in my_list if item > max_num]
        return max_num
