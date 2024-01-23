#!/usr/bin/python3

class Square:
    """Defines a square."""

    def __init__(self, size=0):
        """Initializes the Square instance."""
        self.__size = size

    @property
    def size(self):
        """Represent method to retrieve size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method to set size."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates the area of the square."""
        return self.__size * self.__size
