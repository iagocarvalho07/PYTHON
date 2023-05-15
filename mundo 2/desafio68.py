"""
Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador. 
O jogo só será interrompido quando o jogador perder, 
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

"""
import random

vitorias_consecutivas = 0

while True:
    jogador = int(input("Digite um número: "))
    escolha_jogador = input("Par ou ímpar? ").lower().strip()
    escolha_computador = random.choice(["par", "ímpar"])
    soma = jogador + random.randint(0,5)
    resto = soma % 2

    print(f"O jogador escolheu {jogador} e o computador escolheu {soma - jogador}. Total deu {soma}.")

    if escolha_jogador == escolha_computador:
        if resto == 0:
            print("O jogador ganhou!")
            vitorias_consecutivas += 1
        else:
            print("O computador ganhou!")
            break
    else:
        if resto != 0:
            print("O jogador ganhou!")
            vitorias_consecutivas += 1
        else:
            print("O computador ganhou!")
            break

print(f"Total de vitórias consecutivas: {vitorias_consecutivas}")