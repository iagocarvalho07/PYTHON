"""

Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

"""
from datetime import date

ano_atual = date.today().year
maior = 0
menor = 0
for i in range(1,8):
    ano_nascimento = int(input("digite o ano de nascimento: "))
    idades = ano_atual - ano_nascimento
    if idades > 18:
        maior += 1 
    elif idades < 18:
        menor += 1
print(f"{maior} pessoas são maiores de idade e {menor} pessoas são menor de idade")


