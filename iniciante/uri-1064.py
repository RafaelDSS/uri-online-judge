# -*- coding: utf-8 -*-

numeros = []

for _ in range(6):
    n = float(input())
    numeros.append(n)

numero_positivos = 0
soma_positivos = 0

for numero in numeros:
    if numero > 0:
        numero_positivos += 1
        soma_positivos += numero
print('%d valores positivos' % numero_positivos)
print('%.1f' %(soma_positivos / numero_positivos))
