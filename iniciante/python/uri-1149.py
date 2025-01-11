# -*- coding: utf-8 -*-

v = list(map(int, input().split(" ")))

a = v[0]

for x in v[1:]:
    if x > 0:
        add = lambda x, y: x+y
        seq = list(enumerate([a]*x))
        soma = sum([x+y for x, y in seq])
        print(soma)
        break
