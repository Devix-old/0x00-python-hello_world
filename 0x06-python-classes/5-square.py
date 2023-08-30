#!/usr/bin/python3
"""class that defines a square"""


class Square:
    """class Square"""

    def __init__(self, size=0):
        """Initializes a new square
        Args:
            size (int): The size of the square
        """
        self.__size = size

    @property
    def size(self):
        """getter"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """returns the current square area"""
        return self.__size ** 2

    def my_print(self):
        """print the square"""
        for i in range(self.size):
            for y in range(self.size):
                print("#", end="")
            print()
