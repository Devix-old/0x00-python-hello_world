#!/usr/bin/python3
"""This module define a function that return the sum of two numbers"""


def add_integer(a, b):
    """
    Add two numbers
    Parametres:
    a (int or float): the first number to be added.
    b (int or float, Optional): default 98 and it is seconde number to be add
    Returns:
    int: The sum of 'a' and 'b'

    Raises:
    TypeError if a or b is not an integer or float
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
