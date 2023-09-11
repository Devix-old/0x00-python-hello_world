#!/usr/bin/python3
"""Define inherits_from module"""


def inherits_from(obj, a_class):
    """Define inherits_from function"""
    return isinstance(obj, a_class) and type(obj) is not a_class
