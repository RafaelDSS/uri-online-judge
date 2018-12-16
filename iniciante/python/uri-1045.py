# -*- coding: utf-8 -*-


valores = list(map(float, input().split()))

valores.sort(reverse=True)
a, b, c = valores

no = True

if a >= b+c:
    print('NAO FORMA TRIANGULO')
    no = False

if a**2 == b**2 + c**2 and no:
    print('TRIANGULO RETANGULO')

if a**2 > b**2 + c**2 and no:
    print('TRIANGULO OBTUSANGULO')

if a**2 < b**2 + c**2 and no:
    print('TRIANGULO ACUTANGULO')

if a == b == c and no:
    print('TRIANGULO EQUILATERO')

if a == b and c != a or a == c and b != a or b == c and a != b:
    print('TRIANGULO ISOSCELES')







