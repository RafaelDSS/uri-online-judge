# -*- coding: utf-8 -*-

while True:
    try:
        a = int(input())
    except:
        break
    menor = 12
    for _ in range(a):
        time = float(input())
        if time < menor:
            menor = time
    else:
        print(menor)