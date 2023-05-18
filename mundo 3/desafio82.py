"""
Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. 
Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, 
respectivamente. Ao final, mostre o conteúdo das três listas geradas.
"""

numeros = []
pares = []
impares = []

while True:
    num = int(input('Digite um número: '))
    numeros.append(num)
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break

print('-'*30)
print(f'A lista completa é: {numeros}')
print(f'A lista de pares é: {pares}')
print(f'A lista de ímpares é: {impares}')

