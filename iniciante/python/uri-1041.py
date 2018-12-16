# -*- coding: utf-8 -*-

nums = input().split()

X , Y = float(nums[0]), float(nums[1])

if X == 0.0 and Y == 0.0:
    print('Origem')

elif X == 0.0 and Y != 0.0:
    print('Eixo Y')

elif Y == 0.0 and X != 0.0:
    print('Eixo X')
    
elif X > 0.0 and Y > 0.0:
    print('Q1')
    
elif X < 0.0 and Y > 0.0:
    print('Q2')

elif X < 0.0 and Y < 0.0:
    print('Q3')
    
elif X > 0.0 and Y < 0.0:
    print('Q4')

