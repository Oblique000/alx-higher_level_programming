#!/usr/bin/python3

class Square:
    """Represent a square."""

    def __init__(self, size):
        """Initialize a new square with a given size."""
        self.size = size

    @property
    def size(self):
        """Get the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square."""
        if not isinstance(value, int) or value < 0:
            raise ValueError("size must be a non-negative integer")
        self.__size = value

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square with the # character."""
        for _ in range(self.__size):
            print("#" * self.__size)
        if self.__size == 0:
            print("")
