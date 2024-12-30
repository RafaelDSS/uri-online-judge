# -*- coding: utf-8 -*-

inter = 0
gremio = 0
empate = 0
grenais = 0


def entrada(x):
    return [int(y) for y in x.split(" ")]

while True:
    gols_inter, gols_gremio = entrada(input())
    if gols_inter > gols_gremio:
        inter += 1
    elif gols_gremio > gols_inter:
        gremio += 1
    else:
        empate += 1
    grenais += 1
    opcao = int(input("Novo grenal (1-sim 2-nao)\n"))
    if opcao == 2:
        break


print(f"{grenais} grenais")
print(f"Inter:{inter}")
print(f"Gremio:{gremio}")
print(f"Empates:{empate}")

if inter > gremio:
    print("Inter venceu mais")
elif gremio > inter:
    print("Gremio venceu mais")
else:
    print("Nao houve vencedor")