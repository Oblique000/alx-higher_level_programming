#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    len = len(argv) - 1
    if len < 1:
        print("{} arguments:".format(len))
    elif len == 1:
        print("{} arguments:".format(len))
    else:
        print("{} arguments:".format(len))

        for i in range(len):
            print("{}: {:s}".format(i + 1, argv[i + 1]))
