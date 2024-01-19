#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    mod = len(argv) - 1
    if len < 1:
        print("{} arguments:".format(mod))
    elif mod == 1:
        print("{} arguments:".format(mod))
    else:
        print("{} arguments:".format(mod))
        for i in range(mod):
            print("{}: {:s}".format(i + 1, argv[i + 1]))
