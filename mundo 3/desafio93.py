"""
Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. 
O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. 
No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
"""
golsMarcados = []
JogadorTotal = {}
nome = input("Digite o nome do jogador: ")
partidas = int(input("Quantas partidas esse jogadorou: "))
for i in range(partidas):
    gols = int(input(f"Quantos gols o jogador marcou na partida {i+1}? "))
    golsMarcados.append(gols)

total_de_gols = sum(golsMarcados)

JogadorTotal = {"jogador": nome, "numero de partidas": partidas, "gols": golsMarcados}

print("-" * 30)
print(f"O jogador {JogadorTotal['jogador']} jogou {JogadorTotal['numero de partidas']} partidas no campeonato e marcou um total de {total_de_gols} gols.")

for i, x in enumerate(golsMarcados):
    print(f"No {i + 1}º jogo, o jogador marcou {x} gols")