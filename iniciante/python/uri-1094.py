# -*- coding: utf-8 -*-

N = int(input())

cobaias = {'C': ['coelhos', 0], 'R': ['ratos', 0], 'S': ['sapos', 0]}
total = 0

for _ in range(N):
    qt, tipo = input().split()
    cobaias[tipo][1] += int(qt)
    total += int(qt)

print('Total: %d cobaias' % total)

for cobaia in cobaias:
    c = cobaias[cobaia]
    print('Total de %s: %d' %(c[0], c[1]))

for cobaia in cobaias:
    c = cobaias[cobaia]
    print('Percentual de %s: %.2f %%' %(c[0], (c[1] * 100) / total))
