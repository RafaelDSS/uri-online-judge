# -*- coding: utf-8 -*-

valores = input().split(' ')

A = float(valores[0])
B = float(valores[1])
C = float(valores[2])

PI = 3.14159

TRIANGULO = (A * C) / 2
CIRCULO = PI * (C ** 2)
TRAPEZIO = ((A + B) * C) / 2
QUADRADO = B ** 2
RETANGULO = A * B


print('TRIANGULO: %.3f' % TRIANGULO)
print('CIRCULO: %.3f' % CIRCULO)
print('TRAPEZIO: %.3f' % TRAPEZIO)
print('QUADRADO: %.3f' % QUADRADO)
print('RETANGULO: %.3f' % RETANGULO)
