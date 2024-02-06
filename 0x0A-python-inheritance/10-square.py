#!/usr/bin/python3
"""10-square.py"""
Rectangle = __import__('9-rectangle').Rectangle
"""Rectangle class module"""


class Square(Rectangle):
    """class Square that inherits from Rectangle"""

    def __init__(self, size):
        """The class constructor
        Args:
            size: size of the Square
        """
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Public instance method -
        Calculates the area of the Square
        """
        return self.__size ** 2

    def __str__(self):
        """Return a string representation of the square."""
        return "[Square] {}/{}".format(self.__size, self.__size)
