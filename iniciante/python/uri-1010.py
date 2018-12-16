# -*- coding: utf-8 -*-

var1 = input().split(' ')
var2 = input().split(' ')

TOTAL = (float(var1[2]) * int(var1[1])) + (float(var2[2]) * 
int(var2[1]))

print('VALOR A PAGAR: R$ %.2f' % TOTAL)
