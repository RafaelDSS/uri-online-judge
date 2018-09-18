# -*- coding: utf-8 -*-

N = input().split('.')

valor = int(N[0])

cedulas = (100, 50, 20, 10, 5, 2)


print('NOTAS:')
for cedula in cedulas:

    quant_cedulas = 0

    while valor >= cedula:
        quant_cedulas = valor // cedula
        valor %= cedula
    print('%d nota(s) de R$ %d.00' %(quant_cedulas, cedula))
        


print('MOEDAS:')
if valor == 0:
    print('0 moeda(s) de R$ 1.00')
else:
    print('1 moeda(s) de R$ 1.00')    

valor = int(N[1])
cedulas = (50, 25, 10, 5, 1)

for cedula in cedulas:

    quant_cedulas = 0

    while valor >= cedula:
        quant_cedulas = valor // cedula
        valor %= cedula
    if cedula in [5, 1]:
        print('%d moeda(s) de R$ 0.0%d' %(quant_cedulas, cedula))
    else:
        print('%d moeda(s) de R$ 0.%d' %(quant_cedulas, cedula))
    

