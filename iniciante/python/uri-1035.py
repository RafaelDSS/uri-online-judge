# -*- coding: utf-8 -*-

v = input().split(' ')

A = int(v[0])
B = int(v[1])
C = int(v[2])
D = int(v[3])

if B > C and D > A and (C + D) > (A + B) and C > 0 and D > 0 and A % 2 == 0:
    print('Valores aceitos')
else:
    print('Valores nao aceitos')
