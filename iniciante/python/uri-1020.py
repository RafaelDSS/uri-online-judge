# -*- coding: utf-8 -*-

dias = int(input())

ano, mes, dia = 0, 0, 0

if dias >= 365:
    ano = dias // 365
    dias = dias % 365
if dias >= 30:
    mes = dias // 30
    dias = dias % 30
if dias > 0:
    dia = dias

print('%d ano(s)' % ano)
print('%d mes(es)' % mes)
print('%d dia(s)' % dia)


