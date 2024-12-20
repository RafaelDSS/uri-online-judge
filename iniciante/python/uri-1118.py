# -*- coding: utf-8 -*-

def media_notas():
    qt_notas = 0
    notas_soma = 0

    while qt_notas < 2:
        nota = float(input())
        if nota < 0 or nota > 10:
            print("nota invalida")
            continue
        else:
            notas_soma += nota
            qt_notas += 1
    print(f"media = {(notas_soma / 2):.2f}")

media_notas()
while True:
    x = int(input("novo calculo (1-sim 2-nao)\n"))
    if x == 2:
        break
    elif x != 1:
        continue
    media_notas()
