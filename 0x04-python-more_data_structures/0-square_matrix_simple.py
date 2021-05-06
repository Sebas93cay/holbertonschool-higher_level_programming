#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix is None:
        return []

    def pow2(x): return x * x
    def pow2row(x): return list(map(pow2, x))
    return list(map(pow2row, matrix))
