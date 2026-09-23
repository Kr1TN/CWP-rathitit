#!/usr/bin/env python3
#7.1
def find_the_redheads(family):
    return list(filter(lambda name: family[name] == "red", family))

dupont_family = {
    "rath": "black",
    "khao": "black",
    "virginie": "brown",
    "david": "black",
    "sophie": "red",
}

print(find_the_redheads(dupont_family))