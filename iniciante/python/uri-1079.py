# -*- coding: utf-8 -*-

n = int(input())

for _ in range(n):
    a , b, c = list(map(float, input().split()))
    media = ((2*a) + (3*b) + (5*c)) / 10
    print('%.1f' % media)

