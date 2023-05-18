"""
Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,
guardando tudo em uma lista. No final, mostre:                                            
A) Quantas pessoas foram cadastradas.          
B) Uma listagem com as pessoas mais pesadas.                                                                                                   
C) Uma listagem com as pessoas mais leves.

"""

pessoas = list()
nomeIdade = list()
while True:
    nome = input("digite o nome: ")
    peso = float(input('Digite o peso: '))
    pessoas.append([nome, peso])
    resp = input('Quer continuar? [S/N] ').strip().upper()[0]
    if resp in "Nn":
        break
print(f"foram cadastradas {len(pessoas)} pessoas")
