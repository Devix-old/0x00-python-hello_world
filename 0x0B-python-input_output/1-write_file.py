#!/usr/bin/python3
"""
Module: 1-write_file

Contains a function to write text to a file and returns
the number of characters written.
"""


def write_file(filename="", text=""):
    """
    Writes the specified text to the file and returns the
    number of characters written.

    Args:
        filename (str): The name of the file to be written.
        text (str): The text to be written to the file.

    Returns:
        int: The number of characters written to the file.
    """
    with open(filename, 'w', encoding="utf-8") as f:
        nb = f.write(text)

    return nb
