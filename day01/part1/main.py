#!/usr/bin/env python3

max = 0
cur_max = 0

with open('data.txt') as f:
    for line in f:
        if (line != "\n"):
            cur_max += int(line)
            max = cur_max if cur_max > max else max
        else:
            cur_max = 0
            continue

print(max)