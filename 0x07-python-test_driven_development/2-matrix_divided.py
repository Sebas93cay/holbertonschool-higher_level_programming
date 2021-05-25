#!/usr/bin/python3
"""
divide a matrix module
Functions that divides all items from a matrix by div
"""


def matrix_divided(matrix, div):
    """
    matrix_divided() divide a matrix
    Functions that divides all items from a matrix by div
    """
    if (type(matrix) != list or
            not all(type(row) == list for row in matrix) or
            not all(all(type(a) in [int, float]
                    for a in row) for row in matrix)):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    lens = [len(a) for a in matrix]
    if (not all([lens[0] == l for l in lens])):
        raise TypeError("Each row of the matrix must have the same size")

    if (type(div) not in [int, float]):
        raise TypeError("div must be a number")

    if (div is 0):
        raise ZeroDivisionError("division by zero")

    newMat = [[round(item / div, 2) for item in row] for row in matrix]

    return newMat
