# -*- coding: utf-8 -*-

entrada = input().split()

A = float(entrada[0])
B = float(entrada[1])
C = float(entrada[2])

if A+B > C and A+C > B and B+C > A:

    perimetro = A+B+C
    print('Perimetro = %.1f' % perimetro)
    
else:

    area = ((A+B) * C) / 2
    print('Area = %.1f' % area)
    

