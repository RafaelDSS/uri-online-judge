# -*- coding: utf-8 -*-

a = 0
g = 0
d = 0
saida = 0

while saida != 4:
    entrada = int(input())
    if entrada == 1:
        a += 1
    elif entrada == 2:
        g += 1
    elif entrada == 3:
        d += 1
    if entrada == 4:
        saida = 4

print('MUITO OBRIGADO')
print('Alcool: %d' % a)
print('Gasolina: %d' % g)
print('Diesel: %d' % d)