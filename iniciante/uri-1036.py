# -*- coding: utf-8 -*-

sqrt = lambda x: x ** 0.5

var = input().split(' ')

A = float(var[0])
B = float(var[1])
C = float(var[2])

delta = (B**2)-(4*A*C)

if A != 0 and delta >= 0:
        
    r1 = (-(B) + (sqrt(delta))) / (2*A)
    r2 = (-(B) - (sqrt(delta))) / (2*A)
    
    print('R1 = %.5f\nR2 = %.5f' % (r1, r2))
    
else:
    print('Impossivel calcular')

