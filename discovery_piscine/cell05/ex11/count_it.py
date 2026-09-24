#!/usr/bin/env python3
#./count_it.py "Game" "of" "Thrones"
#5.11
import sys

params = sys.argv[1:]

if len(params) == 0:
    print("none")
else:
    print("parameters: " + str(len(params)))
    for param in params:
        print(param + ": " + str(len(param)))