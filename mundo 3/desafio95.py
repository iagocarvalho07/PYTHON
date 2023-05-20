"""
Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. 
O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. 
No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores, 
incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

"""


Time = []
while True:
    JogadorTotal = {}
    golsMarcados = []

    nome = input("Digite o nome do jogador: ")

    partidas = int(input("Quantas partidas esse jogador jogou: "))

    for i in range(partidas):
        gols = int(input(f"Quantos gols o jogador marcou na partida {i+1}? "))
        golsMarcados.append(gols)

    total_de_gols = sum(golsMarcados)

    JogadorTotal["jogador"] = nome
    JogadorTotal["numero de partidas"] = partidas
    JogadorTotal["gols"] = golsMarcados
    JogadorTotal["GolsTotais"] = total_de_gols

    Time.append(JogadorTotal.copy())

    AdicionarMais = str(input("Deseja adicionar mais algum jogador [S/N]")).upper()

    if AdicionarMais in "Nn":
        break

for k, v in enumerate(Time):
    print(f"O {k+1}° jogador - {v['jogador']}, marcou {v['GolsTotais']} gols no campeonato.")

while True:
    estatistica_individual = str(input("Deseja ver a estatísticas de algum jogador individualmente? [S/N]")).strip().upper()[0]
   
    if estatistica_individual == 'N':
        print("Volte sempre!!")
        break
    elif estatistica_individual == 'S':

        nome_do_jogador = str(input("Digite o nome do jogador que deseja ver as estatísticas individuais por partida: "))
        for jogador in Time:
            if jogador['jogador'] == nome_do_jogador:
                numero_de_partidas = jogador['numero de partidas']
                gols_jogador = jogador['gols']
                print(f"\nEstatísticas do jogador {nome_do_jogador}:")
                for i in range(numero_de_partidas):
                    print(f"Partida {i+1}: {gols_jogador[i]} gols")
                print(f"Total de gols: {sum(gols_jogador)}")
                break
        else:
            print("Jogador não encontrado!")
    else:
        print("Entrada inválida. Digite [S] ou [N]!")