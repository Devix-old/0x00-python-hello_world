#!/usr/bin/python3
"""Square module"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Square(BaseGeometry):
    """Square class : return area of the square"""

    def __init__(self, size):
        self.__size = size
        self.integer_validator("size", size)

    def area(self):
        return self.__size * self.__size

    def __str__(self):
        return str("[Square] {}/{}".format(self.__size, self.__size))
