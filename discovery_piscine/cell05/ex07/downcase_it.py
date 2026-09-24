#!/usr/bin/env python3
#5.7 ./downcase_it.py "LUCIOLE"
#./downcase_it.py "This exercise is quite easy!"

import sys

if len(sys.argv) != 2:
    print("none")
else:
    print(sys.argv[1].lower())