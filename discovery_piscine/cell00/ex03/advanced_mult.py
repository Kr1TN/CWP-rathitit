#!/usr/bin/env python3

import sys

if len(sys.argv) > 1:
    print("none")
else:
    i = 0
    while i <= 10:
        line = "Table de " + str(i) + ": "
        j = 0
        while j <= 10:
            line += str(i * j)
            if j < 10:
                line += " "
            j += 1
        print(line)
        i += 1