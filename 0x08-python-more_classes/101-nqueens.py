#!/usr/bin/python3
"""
N Queens Solver

This module provides a program to solve the N Queens problem and print all possible solutions.

Usage: nqueens N

The program takes one command-line argument, N, which represents the size of the chessboard and the number of queens to be placed.

Module Functions:
    - solve_nqueens(n): Solves the N Queens problem and returns a list of all possible solutions as lists of queen positions.

Function:
    - is_safe(board, row, col, n): Checks if it is safe to place a queen at a given position on the board.
    - solve(board, row): Recursively finds all solutions by backtracking.
"""
import sys


def is_safe(board, row, col, n):
    """
    Check if it is safe to place a queen at a given position on the board.

    Args:
        board (list): The chessboard as a 2D list.
        row (int): The current row to check.
        col (int): The current column to check.
        n (int): The size of the chessboard.

    Returns:
        bool: True if it is safe to place a queen, False otherwise.
    """
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper-left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper-right diagonal
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(n):
    """
    Solve the N Queens problem and return a list of all possible solutions.

    Args:
        n (int): The size of the chessboard and the number of queens.

    Returns:
        list: A list of all possible solutions, where each solution is represented as a list of queen positions.
    """
    if n < 4:
        return []

    def solve(board, row):
        if row == n:
            solutions.append([row[:] for row in board])
            return

        for col in range(n):
            if is_safe(board, row, col, n):
                board[row][col] = 1
                solve(board, row + 1)
                board[row][col] = 0

    solutions = []
    board = [[0 for _ in range(n)] for _ in range(n)]
    solve(board, 0)
    return solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        if n < 4:
            print("N must be at least 4")
            sys.exit(1)

        solutions = solve_nqueens(n)
        for solution in solutions:
            print(solution)

    except ValueError:
        print("N must be a number")
        sys.exit(1)
