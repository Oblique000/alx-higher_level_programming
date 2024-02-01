#!/usr/bin/python3
"""
4-print_square.py
This module prints a square with the character #
"""

def print_square(size):
    """
    Prints a square with the character #.
    
    Raises:
        TypeError: If size is not an integer or a negative float.
        ValueError: If size is less than 0.
    """
    if size is None:
        raise TypeError("missing one argument - size")

    if not isinstance(size, int) or (isinstance(size, float) and size < 0):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)

