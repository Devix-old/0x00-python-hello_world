#!/usr/bin/python3
"""class that defines a square"""


class Square:
    """class Square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a new square
        Args:
            size (int): The size of the square
        """
        self.__position = position
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

    @property
    def position(self):
        """return the current position"""
        return self.__position

    @position.setter
    def position(self, value):
        """set the position"""
        if (not isinstance(value, tuple) or
            not all(isinstance(num, int) for num in value) or
            len(value) != 2 or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """returns the current square area"""
        return self.__size ** 2

    def my_print(self):
        """print the square"""
        if self.__size == 0:
            print()
            return
        for _ in range(self.__position[1]):
            print()
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
