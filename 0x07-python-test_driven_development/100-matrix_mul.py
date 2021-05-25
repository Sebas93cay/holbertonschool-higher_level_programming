#!/usr/bin/python3
"""
Multiply two matrix
"""


def matrix_mul(m_a, m_b):
    """Multiply two matrix"""
    if (type(m_a) != list):
        raise TypeError("m_a must be a list")
    if (type(m_b) != list):
        raise TypeError("m_b must be a list")
    if (any(type(row) != list for row in m_a)):
        raise TypeError("m_a must be a list of lists")
    if (any(type(row) != list for row in m_b)):
        raise TypeError("m_b must be a list of lists")
    if (m_a == [] or m_a == [[]]):
        raise TypeError("m_a can't be empty")
    if (m_b == [] or m_b == [[]]):
        raise TypeError("m_b can't be empty")
    if (any([any([type(item) not in [int, float] for item in row]) for row in m_a])):
        raise TypeError("m_a should contain only integers or floats")
    if (any([any([type(item) not in [int, float] for item in row]) for row in m_b])):
        raise TypeError("m_b should contain only integers or floats")
    if (any([len(m_a[0]) != len(row) for row in m_a])):
        raise TypeError("each row of m_a must be of the same size")
    if (any([len(m_b[0]) != len(row) for row in m_b])):
        raise TypeError("each row of m_b must be of the same size")
    if(len(m_a[0]) != len(m_b)):
        raise ValueError("m_a and m_b can't be multiplied")

    nm_b = []
    for i in range(len(m_b[0])):
        nm_b.append([m_b[j][i] for j in range(len(m_b))])

    res = []
    for i, row_a in enumerate(m_a):
        res.append([])
        for j, column_b in enumerate(nm_b):
            res[i].append(sum([a*b for (a, b) in zip(row_a, column_b)]))

    return res
