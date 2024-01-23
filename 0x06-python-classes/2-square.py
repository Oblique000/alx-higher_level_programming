#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """The class Square represents a square."""
    def __init__(self, size=0):
        """The __init__ is a special method.
        Args:
        size (int): The size of a new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
