"""
Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão.
"""
primeiro_termo = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão da PA: "))
decimo_termo = primeiro_termo + (10 - 1) * razao

for i in range(primeiro_termo, decimo_termo + razao, razao):
    print(i, end=' ')
