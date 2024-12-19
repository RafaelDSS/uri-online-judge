# -*- coding: utf-8 -*-

f = 0

for i in range(1, 12):
    for j in range(1, 4):
        print(f"I={f:g} J={j+f:g}")
    f += 0.2
