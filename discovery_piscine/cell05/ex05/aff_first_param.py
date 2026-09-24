#!/usr/bin/env python3
#5.5 ./aff_first_param.py "Code Ninja" "Numerique" "42"
import sys

if len(sys.argv) > 1:
    print(sys.argv[1])
else:
    print("none")