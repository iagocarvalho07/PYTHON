"""
Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:

5! = 5 x 4 x 3 x 2 x 1 = 120
"""
import math
while True:
    fatorial = int(input("digite um numero para saber seu fatorial: "))
    resultado=1
    count=1

    while count <= fatorial:
        resultado *= count
        count += 1

    print(f"o fatorial de {fatorial} é igual a {resultado}")
