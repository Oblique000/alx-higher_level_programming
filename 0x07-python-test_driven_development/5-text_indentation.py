#!/usr/bin/python3
"""
prints a text with 2 new lines after each
of these characters: ., ? and :.
5-text_indentation.py
"""


def text_indentation(text):
    """prints a text with 2 new lines after
    each of these characters: ., ? and :.

    Args:
        char(list) : containing the characters.
        x(int): keeps track of the number of loops
        lines(list): list containing the splitted string

    Raises:
        TypeError: text must be a string
        ValueError: input must not be an empty string
    """
    if type(text) is not str or text is None:
        raise TypeError("text must be a string")
    if not text.strip():
        raise ValueError("input must not be an empty string")

    char_list = ['.', '?', ':']

    for char in char_list:
        text = text.replace(char + ' ', char + '\n')

    lines = text.split('\n')

    x = 0

    for line in lines:
        stripped_line = line.strip()
        x += 1
        if stripped_line and x < len(lines):
            print(stripped_line)
            print()
        else:
            print(stripped_line, end="")
