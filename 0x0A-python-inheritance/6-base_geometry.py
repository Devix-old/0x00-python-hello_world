#!/usr/bin/python3
"""Define the base_geometry module"""


class BaseGeometry:
    """define class : BaseGeometry
    that raises an Exception with the message area() is not implemented"""

    def area(self):
        raise Exception("area() is not implemented")
