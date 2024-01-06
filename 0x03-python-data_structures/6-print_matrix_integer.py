#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for firstD in matrix:
        n = 0
        for item in firstD:
            print("{:d}".format(item), end='')
            if (n < len(firstD) - 1):
                print(" ", end='')
            n += 1
        print()
