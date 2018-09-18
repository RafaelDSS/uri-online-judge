# -*- coding: utf-8 -*-

X = int(input())

nimpares = 0

while True:
    if X % 2 != 0:
        print(X)
        nimpares += 1
    if nimpares == 6:
        break
    X += 1

