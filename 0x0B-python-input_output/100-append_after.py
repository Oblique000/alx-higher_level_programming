#!/usr/bin/python3
"""Module for appending lines after a specific string in a file."""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file, after each line containing
    a specific string.

    Args:
        filename (str): The name of the file.
        search_string (str): The string to search for.
        new_string (str): The new string to be added to the file.
    """
    try:
        with open(filename, "r", encoding='utf-8') as file:
            lines = file.readlines()

        with open(filename, "w", encoding='utf-8') as file:
            for line in lines:
                file.write(line)
                if search_string in line:
                    file.write(new_string)

        print(f"Lines appended successfully after '{search_string}' in '{filename}'.")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
# append_after("example.txt", "specific_string", "new_line_to_add\n")
