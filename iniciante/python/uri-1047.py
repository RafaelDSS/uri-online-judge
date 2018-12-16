# -*- coding: utf-8 -*-


entrada = input().split()

corretor = 1440

hora_inicio = int(entrada[0])
minuto_inicio = int(entrada[1])
hora_fim = int(entrada[2])
minuto_fim = int(entrada[3])

hora_inicio *= 60
hora_fim *= 60
minuto_inicio += hora_inicio
minuto_fim += hora_fim

if minuto_fim <= minuto_inicio:
    minuto_fim += corretor

print("O JOGO DUROU %d HORA(S) E %d MINUTO(S)" 
%((minuto_fim-minuto_inicio)/60, (minuto_fim-minuto_inicio)%60))

