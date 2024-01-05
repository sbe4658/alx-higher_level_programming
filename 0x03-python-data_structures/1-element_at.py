#!/bin/usr/python3

def element_at(my_list, idx):
    list_range = len(my_list)
    if (idx < 0) or (list_range - 1 < idx):
        return None
    return my_list[idx]
