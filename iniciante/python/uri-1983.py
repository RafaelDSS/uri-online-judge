# -*- coding: utf-8 -*-

M = int(input())

notas = {}

maior = 0
for _ in range(M):
    dados= input().split()
    
    matricula = int(dados[0])
    nota = float(dados[1])
    
    notas[nota] = matricula
    
    if nota > maior:
        maior = nota

if maior >= 8:
    print(notas[maior])
else:
    print('Minimum note not reached')

