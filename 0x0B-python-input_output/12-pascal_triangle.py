#!/usr/bin/python3
"""Module 12: pascal_triangle"""


def pascal_triangle(n):
    """this function return a list of lists of integers representing
    the Pascal’s triangle of n"""
    List = []

    if n <= 0:
        return []
    if n == 1:
        return [[1]]
    if n == 2:
        return [[1], [1, 1]]

    length = 2
    List = [[1], [1, 1]]
    while length != n:
        row = [length]
        temp = List[length - 1]
        row[0] = 1
        for i in range(1, length):
            row.append(temp[i] + temp[i - 1])
        row.append(1)
        List.append(row)

        length += 1

    return List
