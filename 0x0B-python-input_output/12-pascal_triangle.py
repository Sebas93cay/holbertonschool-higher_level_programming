#!/usr/bin/python3
"""
this module has a function that
makes the pascal triangle
"""


def pascal_triangle(n):
    """
    returns a list of lists of
    integers representing the Pascal’s triangle of n
    """
    if n <= 0:
        return []
    triangle = [[1]]
    if n > 1:
        triangle.append([1, 1])
    for i in range(2, n):
        row = [1]
        for j in range(i-1):
            row.append(triangle[i-1][j]+triangle[i-1][j+1])
        row.append(1)
        triangle.append(row)

    return triangle
