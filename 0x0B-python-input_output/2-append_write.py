#!/usr/bin/python3
"""
Module: 2-append_write

Contains a function to append text to a file and returns
number of characters added.
"""


def append_write(filename="", text=""):
    """
    Appends the specified text to the file and returns
    the number of characters added.

    Args:
        filename (str): The name of the file to be appended.
        text (str): The text to be appended to the file.

    Returns:
        int: The number of characters added to the file.
    """
    with open(filename, mode='a', encoding='utf-8') as file:
        nb_characters_added = file.write(text)
    return nb_characters_added
