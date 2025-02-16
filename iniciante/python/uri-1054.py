# -*- coding: utf-8 -*-

qt = 0
sum = 0
while True:
    n = int(input())
    if n < 0:
        print(f"{sum/qt:.2f}")
        break
    qt += 1
    sum += n
