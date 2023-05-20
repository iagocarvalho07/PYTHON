"""
Exercício Python 099: Faça um programa que tenha uma função chamada maior(), 
que receba vários parâmetros com valores inteiros. 
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
"""

def maior(*numeros):
    maior = numeros[0]
    for numero in numeros:
        if numero > maior:
            maior = numero
    print(f'O maior número é: {maior}')

maior(1, 2, 3, 4, 5)
maior(10, 22, 5, 66, 54, 0)
maior(9, 3, 6, 8, 0, -1)