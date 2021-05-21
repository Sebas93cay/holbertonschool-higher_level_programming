#!/usr/bin/python3
"""Solution to the N queens problem"""

import sys


def is_int(n):
    """check if a string is int"""
    try:
        int(n)
        return True
    except:
        return False


def accept(N, sol):
    """
    accept solution to N queen problem if complete is True
    returns true if solution is accepted, False otherwise
    """
    if (len(sol) == N):
        return True
    return False


def reject(sol):
    """return true if sol is not a solution for the problem"""
    # print("inicio de reject")
    last = len(sol) - 1

    for i in range(last):
        if sol[i] == sol[last]:
            return True
        if (last - i) == abs(sol[last] - sol[i]):
            return True
    return False


def next(N, sol):
    """moves last queen one position"""
    last = len(sol) - 1
    if (sol[last] < N - 1):
        sol[last] += 1
        return sol
    sol.pop()
    return None


def first(N, sol):
    """place a new queen"""
    l = len(sol)
    if l == N:
        return None
    sol.append(0)
    return sol


def process(N, sol):
    """recursive process to check posibles solutions from solution"""
    if (reject(sol)):
        return
    if (accept(N, sol)):
        print(str([[x, y] for (x, y) in enumerate(sol)]))
        return
    sol = first(N, sol)
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

    sol = []
    process(N, sol)


main()
