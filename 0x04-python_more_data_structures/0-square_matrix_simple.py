#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = []
    for row in matrix:
        row = list(map(lambda item: item ** 2, row))
        new.append(row)
    return new
