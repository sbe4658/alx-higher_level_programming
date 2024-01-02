#!/usr/bin/python3
n = 1
for c in reversed(range(97, 123)):
    char = c
    if n % 2 == 0:
        char -= 32
    print("{:c}".format(char), end='')
    n += 1
