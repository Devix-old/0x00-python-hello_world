#!/usr/bin/python3
"""class that define a square"""


class Square:
    """class Square"""

    def __init__(self, size=0):
        """Initializes a new square
        Args:
        size (int) : The size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
            

