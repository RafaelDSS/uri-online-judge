# -*- coding: utf-8 -*-

p = 0

for x in range(6):
    n = float(input())
    if n > 0:
        p += 1
        
print('%d valores positivos' % p)
