#!/usr/bin/python3
"""
Module: 0-Read_file

Contains a function to read and print the content of a file.
"""


def read_file(filename=""):
    """
    Reads and prints the content of the specified file.

    Args:
        filename (str): The name of the file to be read.

    Returns:
        None
    """
    with open(filename, 'r', encoding="utf-8") as f:
        read_data = f.read()
    print(read_data, end="")
