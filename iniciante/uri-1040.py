# -*- coding: utf-8 -*-


notas = input().split()

N1, N2, N3, N4 = map(float, notas)

media = ((2*N1)+(3*N2)+(4*N3)+(1*N4)) / sum((2,3,4,1))

print('Media: %.1f' % media)

if media >= 7.0:
    print('Aluno aprovado.')
    
elif media < 5.0:
    print('Aluno reprovado.')

elif media >= 5.0 and media <= 6.9:
    print('Aluno em exame.')
    N5 = float(input())
    
    media2 = (media + N5) / 2
    print('Nota do exame: %.1f' % N5)

    if media2 >= 5.0:
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado.')
    print('Media final: %.1f' % media2)

        

