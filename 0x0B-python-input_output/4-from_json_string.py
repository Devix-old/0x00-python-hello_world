#!/usr/bin/python3
"""
Module: 4-from_json_string

Contains a function to convert a JSON-formatted string to a Python object.
"""

import json


def from_json_string(my_str):
    """
    Converts a JSON-formatted string to a Python object.

    Args:
        my_str (str): The JSON-formatted string to be converted.

    Returns:
        Any: The Python object represented by the JSON string.
    """
    return json.loads(my_str)
