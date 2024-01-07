#!/usr/bin/python3

def no_c(my_string):
    no_c_string = ""
    for idx in range(0, len(my_string)):
        char = my_string[idx]
        if char not in 'Cc':
            no_c_string += char
    return no_c_string
