#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    return ([list(map(lambda num: num * num, row)) for row in matrix])
