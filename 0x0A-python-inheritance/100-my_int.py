#!/usr/bin/python3
"""
This module defines the MyInt class
"""


class MyInt(int):
    """
    MyInt is a custom integer class that inherits from the built-in int class.
    """

    def __eq__(self, other):
        """
        Override the == operator to invert its behavior.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Override the != operator to invert its behavior.

        Args:
            other: The object to compare with MyInt.

        Returns:
            bool: True if the objects are equal, False if they are not equal.
        """
        return super().__eq__(other)
