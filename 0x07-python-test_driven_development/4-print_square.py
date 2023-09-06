#!/usr/bin/python3

"""
This module defines a function to print a square pattern of a specified size.
"""


def print_square(size):
    """
    Print a square pattern of '#' characters with a specified size.

    Parameters:
    size (int): The size of the square. It must be a non-negative integer.

    Returns:
    None

    Raises:
    TypeError: If 'size' is not an integer.
    ValueError: If 'size' is less than 0.
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for y in range(size):
            print("#", end="")
        print()
