#!/usr/bin/python3
"""Solution to the N queens problem"""

import sys


def is_int(n):
    try:
        int(n)
        return True
    except:
        return False

#sol = [[0, 1], [1, 3], [2, 0], [3, 2]]


def accept(N, sol):
    if len(sol) is not N:
        return False
    i = 0
    while i < N - 1:
        j = i + 1
        while j < N:
            if ((sol[i][0] is sol[j][0]) or
                (sol[i][1] is sol[j][1]) or
                (sol[i][0] - sol[j][0] is sol[i][1] - sol[j][1]) or
                    (sol[i][0] - sol[j][0] is sol[j][1] - sol[i][1])):
                return False
            j += 1
        i += 1
    return True


def check_partial_sol(sol, queen):
    """
    check if queen does not attack the queens in sol
    return a list of two elements.
    list[0] is True if queen does not attack anyone, 
    false otherwise.
    list[1] returns the sol with the new queen if it did
    not attack anyone
    """
    for q in sol:
        if ((q[0] is queen[0]) or
            (q[1] is queen[1]) or
            (q[1] - queen[1] is q[0]-queen[0]) or
                (q[1] - queen[1] is queen[0]-q[0])):
            return [False, None]
    sol.append(queen)
    return [True, sol]


def reject(N, sol):
    i = len(sol)
    for j in range(N):
        check = check_partial_sol(sol, [i, j])
        if (check[0]):
            sol = check[1]
            return False


def process(N, sol):
    if (reject(N, sol)):
        return
    print(str(sol))


def main():

    if (len(sys.argv) is not 2):
        print("Usage: nqueens N")
        exit(1)
    N = sys.argv[1]
    if (is_int(N) is False):
        print("N must be a number")
        exit(1)
    N = int(N)
    if (N < 4):
        print("N must be at least 4")
        exit(1)

    #sol = [[x, None] for x in range(N)]
    sol = [[0, 0]]

    process(N, sol)
    print("sol final = "+str(sol))


main()
