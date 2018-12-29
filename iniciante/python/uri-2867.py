# -*- coding: utf-8 -*-

C = int(input())

for _ in range(C):
    s = input().split()
    t = len(str(int(s[0]) ** int(s[1])))
    print('%d' %(t))
