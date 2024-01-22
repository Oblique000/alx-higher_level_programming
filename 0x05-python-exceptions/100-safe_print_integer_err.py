#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    try:
        if not isinstance(value, int):
            raise TypeError("Value must be an integer")
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError) as e:
        print(f"Exception: {e}", file=sys.stderr)
        return (False)
