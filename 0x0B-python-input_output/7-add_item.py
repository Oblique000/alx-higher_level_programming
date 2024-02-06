#!/usr/bin/python3
"""7-add_item module"""
import sys
from os.path import exists
from json import dump, load

filename = "add_item.json"

try:
    my_list = load(open(filename, "r"))
except FileNotFoundError:
    my_list = []

my_list.extend(sys.argv[1:])
dump(my_list, open(filename, "w"))
