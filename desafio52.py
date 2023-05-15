"""
Exercício Python 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
"""
num = int(input("Digite um número inteiro: "))

# Verificar se o número é igual a 2, o único número primo par
if num == 2:
    print("O número", num, "é primo!")
# Verificar se o número é menor que 2 ou par (exceto 2)
elif num < 2 or num % 2 == 0:
    print("O número", num, "não é primo!")
else:
    # Verificar se o número é divisível por algum número ímpar
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            print("O número", num, "não é primo!")
            break
    else:
        print("O número", num, "é primo!")
