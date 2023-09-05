#!/usr/bin/python3
"""Module doc"""


class Rectangle:
    """Rectangle class represents a rectangle with width and height attributes."""

    # Class-level attributes
    number_of_instances = 0  # Number of rectangle instances created
    print_symbol = "#"  # Symbol used for representing the rectangle when printed

    def __init__(self, width=0, height=0):
        """
        Initializes a Rectangle instance with specified width and height.

        Args:
            width (int): The width of the rectangle. Defaults to 0.
            height (int): The height of the rectangle. Defaults to 0.
        """
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """int: The width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Set the width of the rectangle.

        Args:
            value (int): The new width value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """int: The height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle.

        Args:
            value (int): The new height value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculate the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.

        Returns:
            int: The perimeter of the rectangle.
        """
        return 2 * (self.__width + self.__height)

    @classmethod
    def square(cls, size=0):
        """
        Create a square Rectangle instance with equal width and height.

        Args:
            size (int): The size of the square. Defaults to 0.

        Returns:
            Rectangle: A square Rectangle instance.
        """
        return cls(size, size)

    def __str__(self):
        """
        Return a string representation of the rectangle using the print_symbol.

        Returns:
            str: A string representation of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        rectangle_str = ""
        for i in range(self.__height):
            rectangle_str += (str(self.print_symbol) * self.__width)
            if i < self.__height - 1:
                rectangle_str += "\n"
        return rectangle_str

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Compare two Rectangle instances and return the one with a larger or equal area.

        Args:
            rect_1 (Rectangle): The first Rectangle to compare.
            rect_2 (Rectangle): The second Rectangle to compare.

        Returns:
            Rectangle: The Rectangle with a larger or equal area.

        Raises:
            TypeError: If either rect_1 or rect_2 is not an instance of Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    def __repr__(self):
        """
        Return a string representation of the rectangle that can be used to recreate it.

        Returns:
            str: A string representation of the rectangle.
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Destructor method that prints a message when a rectangle instance is deleted."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
