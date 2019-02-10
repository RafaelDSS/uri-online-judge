# -*- coding: utf-8 -*-

I = 1
J = 7
for _ in range(5):
    a = J
    for _ in range(3):
        print('I=%d J=%d' %(I, a))
        a -= 1
    J += 2
    I += 2