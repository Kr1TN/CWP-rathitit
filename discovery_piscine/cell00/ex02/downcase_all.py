#!/usr/bin/env python3
#./downcase_all.py "HELLO WORLD" "I understood Arrays well!"
#6.2
import sys

def downcase_it(string):
    return string.lower()

params = sys.argv[1:]

if len(params) == 0:
    print("none")
else:
    for param in params:
        print(downcase_it(param))