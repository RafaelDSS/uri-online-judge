# -*- coding: utf-8 -*-

c = input().split(' ')

codigo = int(c[0])
quant = int(c[1])

preco = {1:4.00, 2:4.50, 3:5.00, 4:2.00, 5:1.50}

p = preco[codigo] * quant

print('Total: R$ %.2f' %(p))
