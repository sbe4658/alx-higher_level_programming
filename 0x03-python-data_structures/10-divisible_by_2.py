#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    new = [False if item % 2 else True for item in my_list]
    return new
