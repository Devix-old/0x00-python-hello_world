#!/usr/bin/python3
"""Defines the Rectangle module."""

from models.base import Base


class Rectangle(Base):
    """Defines the Rectangle class, a subclass of Base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes a Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The horizontal position. Defaults to 0.
            y (int, optional): The vertical position. Defaults to 0.
            id (int, optional): The identifier. Defaults to None.
        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Getter for width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Getter for height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height."""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getter for x."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x."""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getter for y."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y."""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def update(self, *args, **kwargs):
        """
        Updates the Rectangle attributes.

        Args:
            *args (list): Variable length arguments. If provided:
                - args[0] sets the id.
                - args[1] sets the width.
                - args[2] sets the height.
                - args[3] sets the x position.
                - args[4] sets the y position.
            **kwargs (dict): Keyword arguments. Keys are attribute names.

        Returns:
            None
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.__width = args[1]
            if len(args) >= 3:
                self.__height = args[2]
            if len(args) >= 4:
                self.__x = args[3]
            if len(args) >= 5:
                self.__y = args[4]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def area(self):
        """
        Computes the area of the Rectangle.

        Returns:
            int: The area.
        """
        return self.__width * self.__height

    def display(self):
        """
        Prints the Rectangle with '#' characters.

        Returns:
            None
        """
        print("\n" * self.__y + (" " * self.x +
              ("#" * self.__width) + "\n") * self.__height, end="")

    def to_dictionary(self):
        """
        Returns the dictionary representation of the Rectangle.

        Returns:
            dict: A dictionary containing all Rectangle attributes.
        """
        return self.__dict__

    def __str__(self):
        """
        Returns a string representation of the Rectangle.

        Returns:
            str: A formatted string with Rectangle information.
        """
        return ("[Rectangle] ({}) {}/{} - "
                "{}/{}").format(
            self.id, self.__x, self.__y, self.__width, self.__height)
