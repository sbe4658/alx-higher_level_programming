#!/usr/bin/python3
for x in range(9):
    if x < 8:
        for y in range(x + 1, 10):
            print("{:d}{:d}, ".format(x, y), end='')
    else:
        print("{:d}{:d}".format(x, y))
