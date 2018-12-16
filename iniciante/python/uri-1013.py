# -*- coding: utf-8 -*-

numeros = input().split(' ')

A = int(numeros[0])
B = int(numeros[1])
C = int(numeros[2])

n = (A+B+abs(A-B))/2

MAIOR = n
if n < C:
    MAIOR = C

print('%d eh o maior' % MAIOR)

