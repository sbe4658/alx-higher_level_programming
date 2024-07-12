#!/usr/bin/python3
""" matrix operations. """


def matrix_divided(matrix, div):
    """ devides all elements of matrix.
    Raises:
        TypeError: Matrix is not a list of lists, div is not a number,
        and row sizes is diffrent.
        ZeroDivisionError.
    Return:
        A new matrix contains the remainder matrix elements by ``div``.
    """
    new = []
    err_msg = "matrix must be a matrix (list of lists) of integers/floats"
    if (type(matrix) is not list or not matrix
            or not all(isinstance(r, list) for r in matrix)):
        raise TypeError(err_msg)
    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')
    elif div == 0:
        raise ZeroDivisionError('division by zero')
    item_len = len(matrix[0])
    for item in matrix:
        if not all(isinstance(n, (int, float)) for n in item):
            raise TypeError(err_msg)
        if (item_len != len(item)):
            raise TypeError('Each row of the matrix must have the same size')
        new.append(list(map(lambda n: round(n / div, 2), item)))
    return new
