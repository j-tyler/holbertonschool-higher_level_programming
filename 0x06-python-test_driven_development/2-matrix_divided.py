#!/usr/bin/python3
"""
This module divides a matrix by argument div.
There is one function, matrix_divided().
Returns a new matrix.

>>> matrix_divided([[1, 2], [3, 4]], 2)
[[0.5, 1], [1.5, 2]]
"""


def matrix_divided(matrix, div):
    """
    Returns matrix divided by div. Numbers must be valid ints or floats.
    Numbers are rounded to two decimal places
    """
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists)" +
                        " of integers/floats")

    for row in range(0, len(matrix)):
        if not isinstance(matrix[row], list):
            raise TypeError("matrix must be a matrix " +
                            "(list of lists) of integers/floats")
        if not len(matrix[0]) == len(matrix[row]):
            raise TypeError("Each row of the matrix must have the same size")

        for n in matrix[row]:
            if not isinstance(n, (int, float)):
                raise TypeError("matrix must be a matrix " +
                                "(list of lists) of integers/floats")
    new = [[round(n / div, 2) for n in r] for r in matrix]
    return new
