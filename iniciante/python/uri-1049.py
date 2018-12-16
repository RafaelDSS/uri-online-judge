# -*- coding: utf-8 -*-


dados = []

for _ in range(3):
    entrada = input()
    dados.append(entrada)

animais = {'vertebrado' : {
                         'ave' : {'carnivoro':'aguia', 
'onivoro':'pomba'},
                         
                         'mamifero' : {'onivoro':'homem', 
'herbivoro':'vaca'}
                         },
           
           'invertebrado' : {
                         'inseto' : {'hematofago':'pulga', 
'herbivoro':'lagarta'
                          },
                         'anelideo' : {'hematofago':'sanguessuga', 
'onivoro':'minhoca'}}
           }

a , b , c = dados
print(animais[a][b][c])

