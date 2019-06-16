# -*- coding: utf-8 -*-

N = int(input())

numeros_valor = {1:2, 2:5, 3:5, 4:4, 5:5, 6:6, 7:3, 8:7, 9:6, 0:6}

for _ in range(N):
    numeros = input()
    leds = 0
    for numero in numeros:
        leds += numeros_valor[int(numero)]
    print('%d leds' % leds)
