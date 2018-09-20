# -*- coding: utf-8 -*-


N = int(input())

def eope(N):
    
    if N == 0:
        print('NULL')

    elif N % 2 == 0:
        if N < 0:
            print('EVEN NEGATIVE')
        else:
            print('EVEN POSITIVE')
    else:
        if N < 0:
            print('ODD NEGATIVE')
        else:
            print('ODD POSITIVE')

            
for _ in range(N):
    entrada = int(input())
    eope(entrada)

