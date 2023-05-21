"""
Exercício Python 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas
 aumentar(),
 diminuir(), 
 dobro() 
 metade(). 
 Faça também um programa que importe esse módulo e use algumas dessas funções.
"""

from moduloDesafios import mudulodesafio107

digiteUmNumero = float(input("Digite o preço do produto:R$ "))


mudulodesafio107.aumentar(digiteUmNumero)
print(f" o preço do produto mais 10% e igual a {mudulodesafio107.aumentar(digiteUmNumero)}")
print(f" o dobro do preço do produto e igual a {mudulodesafio107.dobro(digiteUmNumero)}")
print(f" o preço do produto menos 10% e igual a {mudulodesafio107.diminuir(digiteUmNumero)}")
print(f" o preço do produto pela metada e igual a {mudulodesafio107.metade(digiteUmNumero)}")

