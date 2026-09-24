#!/usr/bin/env python3
#./methods_everywhere.py 'lol' 'physically' 'backpack'
#6.4
import sys

def shrink(string):
    return string[:8]

def enlarge(string):
    return string + "Z" * (8 - len(string))

params = sys.argv[1:]

if len(params) < 1:
    print("none")
else:
    for param in params:
        if len(param) > 8:
            print(shrink(param))
        elif len(param) < 8:
            print(enlarge(param))
        else:
            print(param)