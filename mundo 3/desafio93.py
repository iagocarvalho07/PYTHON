"""
Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. 
O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. 
No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
"""
jogador = dict()
gols = list()

nome = str(input("qual o nome do jogador: "))
partidas = int(input("Quantas partidas esse jogador jogou? "))
jogador.update({"nome": nome, "partidas": partidas})
for i in range(partidas):
    gols.append(int(input(f"Quantos gols esse jogar marcou {i+1}° partida: ")))
    
jogador.update({"Numero de gols": gols})
gols.clear()
print(jogador)
print()

