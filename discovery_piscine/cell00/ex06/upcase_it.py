#!/usr/bin/env python3
#./upcase_it.py "initiation"
#./upcase_it.py "This exercise is quite easy!"
#5.6 ./upcase_it.py "initiation"

import sys

if len(sys.argv) != 2:
    print("none")
else:
    print(sys.argv[1].upper())