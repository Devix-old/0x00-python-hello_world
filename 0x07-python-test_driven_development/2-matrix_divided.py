#!/usr/bin/python3

"""
This module defines a function to divide each element of a matrix by a specified divisor.
"""

def matrix_divided(matrix, div):
    """
    Divide each element of a matrix by the specified divisor and return the resulting matrix.

    Parameters:
    matrix (list of lists): The matrix to be divided.
    div (int or float): The divisor by which each element in the matrix will be divided.

    Returns:
    list of lists: The matrix with each element divided by 'div' rounded to 2 decimal places.

    Raises:
    TypeError: If 'div' is not a number, if any element in the matrix is not an integer or float,
               or if rows of the matrix have varying lengths.
    ZeroDivisionError: If 'div' is zero.
    """
    divided_matrix = []

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if matrix:
        first_row = matrix[0]
        for row in matrix[1:]:
            if len(row) != len(first_row):
                raise TypeError("Each row of the matrix must have the same size")
    else:
        return matrix

    for row in matrix:
        divided_row = []
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            divided_row.append(round(element / div, 2))
        divided_matrix.append(divided_row)

    return divided_matrix
