#!/usr/bin/python3
import sys

if __name__ == "__main__":
    len_of_argv = len(sys.argv) - 1

    if len_of_argv >= 1:
        total = sum(int(arg) for arg in sys.argv[1:])
        print(total)
    else:
        print(0))
