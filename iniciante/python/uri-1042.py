# -*- coding: utf-8 -*-


entrada = list(map(int, input().split()))

ordenado = entrada[:]
ordenado.sort()

for valor in ordenado:
    print(valor)
    
print('')

for valor in entrada:
    print(valor)


