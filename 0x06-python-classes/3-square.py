#!/usr/bin/python3

class Square:
    """The class Square defines a square."""

    def __init__(self, size=0):
        """Initialize the new square.

        Args:
            size (int): The size of a new square.
        """
        if not (isinstance(size, int) and size >= 0):
            raise ValueError("size must be a non-negative integer")
        self.__size = size

    def area(self):
        """This returns the area of the Square.

        Returns:
            int: Area of the square.
        """
        return self.__size ** 2

