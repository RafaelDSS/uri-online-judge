# -*- coding: utf-8 -*-

valores = {1:['par(es)', 0],
           2:['impar(es)', 0],
           3:['positivo(s)', 0],
           4:['negativo(s)', 0]
           }

for _ in range(5):
    valor = int(input())
    if valor % 2 == 0:
        valores[1][1] += 1
    else:
        valores[2][1] += 1
    
    if valor > 0:
        valores[3][1] += 1
    elif valor < 0:
        valores[4][1] += 1

for valor in valores:
    print('%d valor(es) %s' %(valores[valor][1], valores[valor][0]))