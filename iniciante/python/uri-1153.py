# -*- coding: utf-8 -*-

n = int(input())

def fatorial(num):
    if num == 0:
        return 1
    return num * fatorial(num - 1)

print(fatorial(n))
