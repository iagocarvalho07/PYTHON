"""
Exercício Python 103: Faça um programa que tenha uma função chamada ficha(), 
que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. 
O programa deverá ser capaz de mostrar a ficha do jogador
mesmo que algum dado não tenha sido informado corretamente.
Aula Ant
"""
def ficha(Jogador='Desconhecido', gols=0):
    print(F" o {Jogador} fez {gols} no campeonto")


nome_jogador = str(input("digite o nome do jogador: "))
gols_jogador = int(input("Quantos gols esse jogador fez: "))

ficha(nome_jogador, gols_jogador)