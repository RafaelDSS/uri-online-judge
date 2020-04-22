# -*- coding: utf-8 -*-

maior = 0
posicao = 0

for pos in range(100):
    numero = int(input())
    if numero > maior:
        maior = numero
        posicao = pos + 1

print(maior)
print(posicao)
