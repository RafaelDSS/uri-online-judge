# -*- coding: utf-8 -*-

cpf = input()

p = cpf.split('-')

for n in p[0].split('.'):
    print(n)
print(p[1])
