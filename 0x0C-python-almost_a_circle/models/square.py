#!/usr/bin/python3
"""Defines the Square module."""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines the Square class, a subclass of Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a Square instance.

        Args:
            size (int): The size of the square (width and height).
            x (int, optional): The horizontal position. Defaults to 0.
            y (int, optional): The vertical position. Defaults to 0.
            id (int, optional): The identifier. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for size."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Updates the Square attributes.

        Args:
            *args (list): Variable length arguments. If provided:
                - args[0] sets the id.
                - args[1] sets the size.
                - args[2] sets the x position.
                - args[3] sets the y position.
            **kwargs (dict): Keyword arguments. Keys are attribute names.

        Returns:
            None
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Returns the dictionary representation of the Square.

        Returns:
            dict: A dictionary containing all Square attributes.
        """
        return {'id': self.id, 'x': self.x, 'size': self.size, 'y': self.y}

    def __str__(self):
        """
        Returns a string representation of the Square.

        Returns:
            str: A formatted string with Square information.
        """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.size)
