# -*- coding: utf-8 -*-

valor = int(input())

cedulas = (100, 50, 20, 10, 5, 2, 1)

print(valor)
for cedula in cedulas:

    quant_cedulas = 0

    while valor >= cedula:
        quant_cedulas = valor // cedula
        valor %= cedula
    print('%d nota(s) de R$ %d,00' %(quant_cedulas, cedula))
