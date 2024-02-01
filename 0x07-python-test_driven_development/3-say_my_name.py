#!/usr/bin/python3
"""
say_my_name: This module prints My name is <first name> <last name>.
"""

def say_my_name(first_name, last_name=""):
    """
    Prints My name is <first name> <last name>.

    Raises:
        TypeError: If first_name or last_name is not a string containing letters.
    """
    if not isinstance(first_name, str) or not first_name.isalpha():
        raise TypeError("first_name must be a string containing letters")

    if last_name and (not isinstance(last_name, str) or not last_name.isalpha()):
        raise TypeError("last_name must be a string containing letters")

    print("My name is {} {}".format(first_name, last_name))
