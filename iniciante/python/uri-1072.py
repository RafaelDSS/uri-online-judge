# -*- coding: utf-8 -*-

N = int(input())

v_in = 0
v_out = 0

for _ in range(N):
    X = int(input())
    if X >= 10 and X <= 20:
        v_in += 1
    else:
        v_out += 1
print('%d in' % v_in)
print('%d out' % v_out)