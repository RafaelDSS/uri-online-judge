# -*- coding: utf-8 -*-


salario = float(input())

taxa = 4

if salario <= 400:
    taxa = 15
elif salario <= 800:
    taxa = 12
elif salario <= 1200:
    taxa = 10
elif salario <= 2000:
    taxa = 7

reajuste = (salario * taxa) / 100
total_salario = salario + reajuste

print('Novo salario: %.2f' % total_salario)
print('Reajuste ganho: %.2f' % reajuste)
print('Em percentual: %d %%' % taxa)

