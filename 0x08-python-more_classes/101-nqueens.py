#!/usr/bin/python3
"""This module prints all the possible combinations one can make to solve
the N queens problem. That is, given an N*N 'chess' board, what are the
positions of N queens so that no queens threat each other's position.

Because this is a recursive solution using backtracking, the time complexity
is bound to be O(N!), which means, for a board more than 25 * 25 this algorithm
may perform poorly
"""


def backtrack_queens(N, current, queens_pos):
    """The actual backtracking function.

    Goes through the whole N * N board putting queens.
    If a position is valid for the current queen, the function calls itself
    with the next queen to be put. If not, then the queen moves to the next
    position removing the current one from the valid position array.

    Args:
        N (int): The size of the board.
        current (int): The position of the current queen.
        queen_pos (:obj:`list` of :obj:`int`): The array of queen positions to
                                               be put.
    """
    if (current == N):
        print([[r, c] for r, c in enumerate(queens_pos)])
    else:
        for col in range(N):
            queens_pos.append(col)
            if (valid_position(queens_pos, current)):
                backtrack_queens(N, current + 1, queens_pos)
            queens_pos.pop(-1)


def valid_position(queens_pos, current):
    """Checks if the position of the current queen is valid.

    If the row of one of the past queens coincides with the current one,
    returns False.

    If the diagonal of one of the past queens coincides with the current one,
    returns False.

    Returns:
        bool: True if valid, False otherwise.
    """
    for i in range(current):
        if queens_pos[i] == queens_pos[current]:
            return False
        if current - i == abs(queens_pos[current] - queens_pos[i]):
            return False
    return True


if __name__ == '__main__':
    from sys import argv

    if (len(argv) != 2):
        print("Usage: nqueens N")
        exit(1)

    try:
        N = int(argv[1])
    except ValueError:
        print("N must be a number")
        exit(1)

    if (N < 4):
        print("N must be at least 4")
        exit(1)

    queens_pos = []
    backtrack_queens(N, 0, queens_pos)
