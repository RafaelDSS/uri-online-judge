# -*- coding: utf-8 -*-

n1 = int(input())
n2 = int(input())

if n1 > n2:
    n1, n2 = n2, n1

sum = 0
for x in range(n1, n2 + 1):
    if x % 13 != 0:
        sum += x

print(sum)
