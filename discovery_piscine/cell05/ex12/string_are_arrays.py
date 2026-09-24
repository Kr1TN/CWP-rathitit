#!/usr/bin/env python3

#./string_are_arrays.py "The character Z is not found in this string"
#./string_are_arrays.py "The character z is found in this string"
#./string_are_arrays.py "Zaz visits the zoo with Zazie"

import sys

if len(sys.argv) != 2:
    print("none")
else:
    text = sys.argv[1]
    count = text.count("z")
    if count == 0:
        print("none")
    else:
        print("z" * count)