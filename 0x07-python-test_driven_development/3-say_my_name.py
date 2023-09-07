#!/usr/bin/python3
"""
This module defines a function to print a person's name.
"""


def say_my_name(first_name, last_name=""):
    """
    Print a person's name based on their first name and
    optionally their last name.

    Parameters:
    first_name (str): The person's first name.
    last_name (str, optional): The person's last
    name. Default is an empty string.

    Returns:
    None

    Raises:
    TypeError: If 'first_name' or 'last_name' is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    if last_name:
        print(f"My name is {first_name} {last_name}")
    else:
        print(f"My name is {first_name} ")
