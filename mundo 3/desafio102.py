"""
Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) 
indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

"""

def fatorial(numero, show=False):
    sum = 1
    for i in range(numero, 0, -1):
        sum *=i
    if show:
        print(F"o fatorial do numero {numero} é {sum}")
        print("e o processo que leva a isso é ")
        for i in range(numero, 0, -1):
            print(F"{i} x ", end=" ")
        print(F" = {sum}", end=" ")
    else:
        print(F"o fatorial do numero {numero} é {sum}")
        

digiteN1 = int(input("digite um numero inteiro para saber seu fatorial "))
while True:
    digiteN2 = str(input("deseja mostrar o processo do fatorial [S/N ?")).upper()
    if digiteN2 in "Ss":
        print("mostrando o fatorial: ")
        fatorial(digiteN1, True)
        break
    elif digiteN2 in "Nn":
        print("optou por nao mostrar o fatorial ")
        fatorial(digiteN1)
        break
    else:
        print("Digite um valor valido")