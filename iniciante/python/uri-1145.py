# -*- coding: utf-8 -*-

x, y = [int(x) for x in input().split(" ")]

line = x
for a in range(1, y + 1):
    if a == line:
        print(a)
        line += x
    else:
        print(a, end=" ")
