#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        char = ord(str[i])
        for lower in range(97, 123):
            if lower == char:
                char -= 32
        print("{:c}".format(char), end='')
    else:
        print()
