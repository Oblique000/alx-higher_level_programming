#!/usr/bin/python3
"""103-magic_class.py"""
import math


class MagicClass:
    """Determines the area and circumference of a circle."""
    def __init__(self, radius=0):
        """Initialize the MagicClass instance with a given radius.

        Args:
            radius (int or float): The radius of the circle.
        """
        self.__radius = 0
        if not isinstance(radius, (int, float)):
            raise TypeError("radius must be a number")
        self.__radius = float(radius)

    def area(self):
        """Calculate and return the area of the circle.

        Returns:
            float: The calculated area of the circle.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Calculate and return the circumference of the circle.

        Returns:
            float: The calculated circumference of the circle.
        """
        return 2 * math.pi * self.__radius
