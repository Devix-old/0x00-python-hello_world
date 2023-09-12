#!/usr/bin/python3
"""
Module: 3-to_json_string

Contains a function to convert a Python object to a JSON-formatted string.
"""

import json


def to_json_string(my_obj):
    """
    Converts a Python object to a JSON-formatted string.

    Args:
        my_obj: The Python object to be converted.

    Returns:
        str: The JSON-formatted string representation of the object.
    """
    return json.dumps(my_obj)
