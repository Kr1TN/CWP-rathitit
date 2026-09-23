#!/usr/bin/env python3
#./scan_it.py "the" "the quick brown fox jumps over the lazy dog"
#5.9
import sys

if len(sys.argv) != 3:
    print("none")
else:
    keyword = sys.argv[1]
    text = sys.argv[2]
    count = text.count(keyword)
    if count == 0:
        print("none")
    else:
        print(count)