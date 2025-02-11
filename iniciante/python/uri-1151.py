# -*- coding: utf-8 -*-

n = int(input())

n1 = 0
n2 = 1

print("0", end="")
for x in range(n-1):
    n1, n2, = n2, n1 + n2
    print(f" {n1}", end="")
print()
