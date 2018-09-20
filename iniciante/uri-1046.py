# -*- coding: utf-8 -*-


entrada = input().split()

inicio = int(entrada[0])
fim = int(entrada[1])

hora = 0
if inicio > fim:
    fim += 24

if inicio == fim:
    hora = 24

else:
    hora = fim - inicio

print('O JOGO DUROU %d HORA(S)' % hora)
    

