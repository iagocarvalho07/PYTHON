###Exercício Python 19: Um professor quer sortear um dos seus quatro alunos para apagar o quadro. 
###Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

import random
n1 = input('digite o nome do primeiro aluno: ')
n2 = input('digite o nome do segundo aluno: ')
n3 = input('digite o nome do terceiro aluno: ')
n4 = input('digite o nome do quarto aluno: ')
lista = [n1, n2, n3, n4]

rand = random.choice(lista)
print('o nome escolhido foi {}'.format(rand))