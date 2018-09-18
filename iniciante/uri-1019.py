# -*- coding: utf-8 -*-

segundos = int(input())

hora, minuto, segundo = 0, 0, 0

if segundos >= 3600:
     hora = segundos // (60*60)
     segundos = segundos % (60*60)

if segundos >= 60:
         minuto = segundos // 60
         segundos = segundos % 60
         
if segundos > 0:
             segundo = segundos
print('%d:%d:%d' %(hora, minuto, segundo))
