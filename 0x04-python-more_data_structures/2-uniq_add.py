#!/usr/bin/python3
from functools import reduce


def uniq_add(my_list=[]):
    return reduce(lambda n1, n2: n1 + n2, my_list)
