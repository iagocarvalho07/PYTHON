"""
Exercício Python 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas
 aumentar(),
 diminuir(), 
 dobro() 
 metade(). 
 Faça também um programa que importe esse módulo e use algumas dessas funções.
"""

def aumentar(nun):
    return nun *1.10


def diminuir(nun1):
    return nun1*0.90
    

def dobro(nuns):
    return nuns*2

def metade(meta):
    return meta / 2
    

def moeda(preco =0 , moeda ="R$"):
    return f"{moeda}{preco}".replace(".", ",")