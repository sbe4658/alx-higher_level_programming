#!/usr/bin/python3
for x in range(10):
    for y in range(10):
        if x < 9 or y < 9:
            print("{:d}{:d}, ".format(x, y), end='')
        else:
            print("{:d}{:d}".format(x, y))
