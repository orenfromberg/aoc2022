#!/usr/bin/env python3

sum = 0
max = 0
with open('./day01/part1/data.txt') as f:
    for line in f:
        sum = sum + int(line) if line != "\n" else 0
        max = sum if sum > max else max
print(max)