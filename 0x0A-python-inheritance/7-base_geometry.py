#!/usr/bin/python3
"""7-base_geometry module"""


class BaseGeometry:
    """This is the  BaseGeometry class"""
    def area(self):
        """Public instance method -
        that raises an Exception with the message
        area() is not implemented
        Raises:
            Exception: area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Public instance method.
        validates value.
        Raises:
            TypeError: name must be a string
            TypeError: name must not be an empty string
            TypeError: "{} must be an integer".format(name)"
            VlaueError: "{} must be greater than 0".format(name)"
        """
        if not isinstance(name, str):
            raise TypeError("name must be a string")

        if not name or not isinstance(name, str):
            raise TypeError("name must not be an empty string")

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
