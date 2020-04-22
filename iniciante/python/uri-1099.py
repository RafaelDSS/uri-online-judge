# -*- coding: utf-8 -*-

N = int(input())

valores = []

for _ in range(N):
    X, Y = list(map(int, input().split()))
    if X > Y:
        X, Y = Y, X
    soma = 0
    for numero in range(X+1, Y):
        if not numero % 2 == 0:
            soma += numero
    valores.append(soma)

for vals in valores:
    print(vals)