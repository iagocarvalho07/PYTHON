"""
Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

"""

num = int(input("Digite um número inteiro: "))  # pedir para o usuário digitar um número inteiro
print("Escolha qual base de conversão: ")  
print("1 - Binário")
print("2 - Octal")
print("3 - Hexadecimal")
opcao = int(input("Opção escolhida: "))  # pedir para o usuário escolher uma opção

if opcao == 1:
    print(f"{num} em binário = {bin(num)[2:]}")  # converter para binário e imprimir
elif opcao == 2:
    print(f"{num} em octal = {oct(num)[2:]}")  # converter para octal e imprimir
elif opcao == 3:
    print(f"{num} em hexadecimal = {hex(num)[2:]}")  # converter para hexadecimal e imprimir
else:
    print("Opção inválida!")  # caso a opção escolhida não seja 1, 2 ou 3
