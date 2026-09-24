#!/usr/bin/env python3

print("Enter a number")
number = int(input())

for i in range(10):
    print(str(i) + " x " + str(number) + " = " + str(i * number))