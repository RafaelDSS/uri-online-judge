# -*- coding: utf-8 -*-

n1 = int(input())
n2 = int(input())

if n1 > n2:
    n1, n2 = n2, n1

for x in range(n1 + 1, n2):
    y = x % 5
    if y == 2 or y == 3:
        print(x)
