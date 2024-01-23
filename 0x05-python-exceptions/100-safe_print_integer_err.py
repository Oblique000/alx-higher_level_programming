#!/usr/bin/python3

import sys

def safe_print_integer_err(value):
    try:
        print(f"{int(value)}")
        return (True)
    except (TypeError, ValueError) as e:
        print(f"Exception: {e}", file=sys.stderr)
        return (False)
