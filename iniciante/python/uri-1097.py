# -*- coding: utf-8 -*-

start_seq = 5

for i in range(1, 10, 2):
    for j in range(start_seq, start_seq + 3)[::-1]:
        print(f"I={i} J={j}")
    start_seq += 2

