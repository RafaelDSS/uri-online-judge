# -*- coding: utf-8 -*-

casos = int(input())

for x in range(casos):
    number = int(input())
    for n in range(2, number):
        if number % n == 0:
            print('%d nao eh primo' % number)
            break
    else:
        print('%d eh primo' % number)
