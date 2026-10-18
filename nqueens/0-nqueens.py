#!/usr/bin/python3
"""Module that solves the N queens puzzle and prints every solution."""
import sys


def solve(n: int, row: int, cols: set, diag1: set, diag2: set,
          board: list) -> None:
    """Place queens row by row using backtracking and print each
    complete placement of N non-attacking queens."""
    if row == n:
        print(board)
        return
    for col in range(n):
        if col in cols or (row - col) in diag1 or (row + col) in diag2:
            continue
        cols.add(col)
        diag1.add(row - col)
        diag2.add(row + col)
        board.append([row, col])
        solve(n, row + 1, cols, diag1, diag2, board)
        board.pop()
        cols.remove(col)
        diag1.remove(row - col)
        diag2.remove(row + col)


def main() -> None:
    """Validate the command-line argument and start solving the puzzle
    for the given board size."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    solve(n, 0, set(), set(), set(), [])


if __name__ == "__main__":
    main()
