# -*- coding: utf-8 -*-

saida = []
while True:
    M, N = list(map(int, input().split()))
    if N <= 0 or M <= 0:
        break
    if N > M:
        M, N = N, M
    vals = ''
    soma = 0
    for s in range(N, M+1):
        soma += s
        vals += str(s) + ' '
    saida.append('%sSum=%d' %(vals, soma))

for output in saida:
    print(output)