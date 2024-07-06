#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == []:
        return None
    x = y = 0
    for data in my_list:
        score = data[0]
        weight = data[1]
        x += (score * weight)
        y += weight
    return x / y
