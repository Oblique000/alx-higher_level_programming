#!/usr/bin/python3

class Square:
    """The class Square defines a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new square with a given size and position."""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Get the current position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square."""
        if (
                (type(value) is not tuple) or (len(value) != 2) or
                (type(value[0]) is not int) or (type(value[1]) is not int) or
                (value[0] < 0) or (value[1] < 0)
                ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square with the character '#'."""
        if self.__size == 0:
            print()
        else:
            print('\n' * self.__position[1], end='')
            for _ in range(self.__size):
                print(' ' * self.__position[0] + '#' * self.__size)
