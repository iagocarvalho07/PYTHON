"""
Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,
guardando tudo em uma lista. No final, mostre:                                            
A) Quantas pessoas foram cadastradas.          
B) Uma listagem com as pessoas mais pesadas.                                                                                                   
C) Uma listagem com as pessoas mais leves.

"""

pessoas = []
while True:
    nome = input('Digite o nome: ')
    peso = float(input('Digite o peso: '))
    pessoas.append([nome, peso])
    resp = input('Quer continuar? [S/N] ').strip().upper()[0]
    if resp == 'N':
        break
    
print(f'Foram cadastradas {len(pessoas)} pessoas.')
maior = menor = pessoas[0][1]
maior_pessoas = []
menor_pessoas = []
for p in pessoas:
    if p[1] > maior:
        maior = p[1]
    if p[1] < menor:
        menor = p[1]
for p in pessoas:
    if p[1] == maior:
        maior_pessoas.append(p[0])
    if p[1] == menor:
        menor_pessoas.append(p[0])
print(f'O maior peso foi de {maior}kg. Peso de {maior_pessoas}.')
print(f'O menor peso foi de {menor}kg. Peso de {menor_pessoas}.')


