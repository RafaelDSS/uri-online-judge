# -*- coding: utf-8 -*-

n = int(input())
for _ in range(n):
    x, y = [int(j) for j in input().split(" ")]
    if y == 0:
        print("divisao impossivel")
    else:
        print(f"{x/y:.1f}")