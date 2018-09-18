# -*- coding: utf-8 -*-

v1 = input().split(' ')
v2 = input().split(' ')

x1 = float(v1[0])
y1 = float(v1[1])

x2 = float(v2[0])
y2 = float(v2[1])

valor = (((x2 - x1)**2) + ((y2 - y1)**2)) ** 0.5
print('%.4f' % valor)
