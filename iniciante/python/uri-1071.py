# -*- coding: utf-8 -*-

v2 = int(input())
v1 = int(input())

soma = 0

for valor in range(v1+1, v2):
    print(soma)
    if valor % 2 != 0:
        soma += valor
print(soma)
