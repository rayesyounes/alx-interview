#!/usr/bin/python3
"""nqueens"""
import sys


def backtrack(r, n, cols, pos, neg, board):
    """Backtracking function to find all possible solutions"""
    if r == n:
        res = []
        for i in range(len(board)):
            for k in range(len(board[i])):
                if board[i][k] == 1:
                    res.append([i, k])
        print(res)
        return

    for c in range(n):
        if c in cols or (r + c) in pos or (r - c) in neg:
            continue

        cols.add(c)
        pos.add(r + c)
        neg.add(r - c)
        board[r][c] = 1

        backtrack(r + 1, n, cols, pos, neg, board)

        cols.remove(c)
        pos.remove(r + c)
        neg.remove(r - c)
        board[r][c] = 0


def nqueens(n):
    """
    Solution
    Args:
        n (int): number of queens. Must be >= 4
    Return:
        List of lists representing coordinates of each
        queen for all possible solutions
    """
    cols = set()
    pos_diag = set()
    neg_diag = set()
    board = [[0] * n for i in range(n)]

    backtrack(0, n, cols, pos_diag, neg_diag, board)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
        if n < 4:
            print("N must be at least 4")
            sys.exit(1)
        nqueens(n)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
