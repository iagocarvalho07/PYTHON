"""
Exercício Python 096: Faça um programa que tenha uma função chamada área(), 
que receba as dimensões de um terreno retangular 
(largura e comprimento) e mostre a área do terreno.
"""

def are(x, y):
    print(f"a dimenção do terreno e igual a {x*y} metros Quadrados  ")


l = float(input("digite a largura do terreno: "))
c = float(input("digite o comprimento do terreno"))
are(l,c)