# -*- coding: utf-8 -*-

N = int(input())

for numero in range(2, N+1):
    if numero % 2 == 0:
        quadrado = numero ** 2
        print('%d^2 = %d' %(numero, quadrado))
