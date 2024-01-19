#!/usr/bin/python3
def uppercase(str):
    for x in str:
        if ord('a') <= ord(x) <= ord('z'):
            upper_case = chr(ord(x) - 32)
        else:
            upper_case = x
        print("{}".format(upper_case), end="")
    print()
