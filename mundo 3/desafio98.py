"""
Exercício Python 098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo. 
Seu programa tem que realizar três contagens através da função criada:
a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada
"""

def contador(inicio, fim, passo):
    for x in range(1, 10, 1):
        print(f" {x} ", end="")
    print()
    for y in range(10, 0, -2):
        print(f" {y} ", end="")
    print()
    for personalizada in range(inicio, fim, passo):
        print(f" {personalizada} ", end="")

iniciar = int(input("digite um numero inteiro para iniciar a contagem: "))
ateOnde = int(input("até que numero gostaria que a contagem fosse: "))
passoApasso = int(input("a contagem deve ir de quantos em quantos passos ? "))

contador(iniciar, ateOnde, passoApasso)

