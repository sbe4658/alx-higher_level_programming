#!/usr/bin/python3
def search_replace(my_list, search, replace):
    # iterate throgh the list
    # Check if search is in the list
    # replace search
    result = []
    result = list(map(lambda n: replace if n == search else n, my_list))
    return result
