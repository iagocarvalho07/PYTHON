"""
Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo
desconsiderando os espaços. Exemplos de palíndromos:

"""

frase = input('Digite uma frase: ').replace(' ', '').lower()
if frase == frase[::-1]:
    print('A frase digitada é um palíndromo!')
else:
    print('A frase digitada não é um palíndromo.')