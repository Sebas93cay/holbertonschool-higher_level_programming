#!/usr/bin/python3
"""Solution to the N queens problem"""

import sys
from typing import SupportsComplex


def is_int(n):
    """check if a string is int"""
    try:
        int(n)
        return True
    except:
        return False

# sol = [[0, 1], [1, 3], [2, 0], [3, 2]]


def copy_sol(solution):
    """return copy of list of lists"""
    sol = []
    for i in solution:
        sol.append(i[:])
    return sol


def accept(N, sol, complete):
    """
    accept solution to N queen problem if complete is True
    returns true if solution is accepted, False otherwise


    if complete is false, just check wheter all the queens are
    in "peace" to eache other"
    returns True if peace exist, false otherwise
    """
    if ((len(sol) is not N) and complete):
        return False
    i = 0
    N = len(sol)
    # print("in accept N is now = {}".format(N))
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
    check if queen does not attack the queens in sol.
    In case queen does not attack anyone its appended to sol
    return True if queen does not attack anyone,
    false otherwise.
    """
    for q in sol:
        if ((q[0] is queen[0]) or
            (q[1] is queen[1]) or
            (q[1] - queen[1] is q[0]-queen[0]) or
                (q[1] - queen[1] is queen[0]-q[0])):
            return False
    sol.append(queen)
    return True


def reject(N, sol):
    """return true if sol is not a solution for the problem"""
    # print("inicio de reject")
    if (accept(N, sol, False) is False):
        return False
    # print("despues de accept en reject")
    i = len(sol)
    for j in range(N):
        if (check_partial_sol(sol, [i, j])):
            # print("first = "+str(sol))
            return False
    # print("final de reject")
    return True


def next(N, solution):
    """return next posible solution after solution"""
    i = len(solution) - 1

    if (solution[i][1] is N - 1):
        # print(str(solution)+" no tiene posible next")
        return None
    sol = copy_sol(solution)
    sol[i][1] += 1
    while(sol[i][1] < N):
        if accept(N, sol, False):
            # print("next = "+str(sol))
            return sol
        sol[i][1] += 1
    # print(str(solution)+" no tiene posible next")
    return None


def process(N, solution):
    """recursive process to check posibles solutions from solution"""
    sol = copy_sol(solution)
    if (reject(N, sol)):
        return
    if (accept(N, sol, True)):
        print(str(sol))
        return
    while (sol is not None):
        process(N, sol)
        sol = next(N, sol)


def main():
    """main function"""
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

    # sol = [[x, None] for x in range(N)]
    # sol = [[0, 0], [1, 2], [2, 0]]
    sol = []

    process(N, sol)

    # print("sol final = "+str(sol))


main()
