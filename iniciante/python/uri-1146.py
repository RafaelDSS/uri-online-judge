# -*- coding: utf-8 -*-

while True:
    x = int(input())
    if x == 0:
        break
    for y in range(1, x):
        print(y, end=" ")
    print(x)
