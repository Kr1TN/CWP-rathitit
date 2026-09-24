#!/usr/bin/env python3
#./aff_rev_params.py "coucou"
#./aff_rev_params.py "Python" "piscine" "hello"
#5.8
import sys

params = sys.argv[1:]

if len(params) < 2:
    print("none")
else:
    for param in reversed(params):
        print(param)