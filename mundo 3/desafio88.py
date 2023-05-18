"""
Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, 
cadastrando tudo em uma lista composta.
"""
import random

megaSena = list()
quantosJogos = int(input("quantos jogos vc quer que eu sorteie: "))
for j in range(quantosJogos):
    for i in range(0,6):
        megaSena.append(random.randint(1,60))
    megaSena.sort()
    print(f" o {j+1}° jogo tem os numeros :{megaSena}")
    megaSena.clear()