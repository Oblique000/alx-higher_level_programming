#!/usr/bin/python3

class Square:
    """The class Square defines a square."""

    def __init__(self, size=0):
        """Initialize the Square instance.

        Args:
            size (int): The size of the square (default is 0).
        """
        self.__size = 0
        self.size = size

    @property
    def size(self):
        """Get the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value (int): The new size value.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate the area of the square."""
        return self.__size ** 2
