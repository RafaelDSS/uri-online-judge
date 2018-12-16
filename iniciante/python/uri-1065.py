# -*- coding: utf-8 -*-

n = 0
npares = 0

while n < 5:
    numero = int(input())
    if numero % 2 == 0:
        npares += 1
    n += 1
print('%d valores pares' % npares)

