"""
Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

a) Os 5 primeiros times.

b) Os últimos 4 colocados.

c) Times em ordem alfabética.

d) Em que posição está o time da Chapecoense.
"""
times_brasileirao = ('Red Bull Bragantino', 'Athletico-PR', 'Fortaleza', 'Atlético-MG', 'Corinthians', 
                     'Flamengo', 'Fluminense', 'São Paulo', 'Cuiabá', 'Internacional', 
                     'Sport Recife', 'Juventude', 'Santos', 'Ceará', 'Palmeiras', 'América-MG', 
                     'Grêmio', 'Bahia', 'Atlético-GO', 'Chapecoense')

while True:
    escolha = int(input("""
    digite o que vc quer ver do campeonato brasileir
    [1] - Os 5 primeiros times.
    [2] - Os últimos 4 colocados.
    [3] - Times em ordem alfabética.
    [4] - Em que posição está o time da Chapecoense.
    """))
    if escolha == 1:
        print (f" os 5 primeiros colocados são")
     #   for i in range(0, len(times_brasileirao)-15):
     #       print (f" {i+1} {times_brasileirao[i]}")
        i = 0
        while i < 5 :
           print (f" {i+1} {times_brasileirao[i]}")
           i += 1
    elif escolha == 2:
        print (f" os ultimos 4 colocados são")
        for i in range(16, len(times_brasileirao)):
            print (f" {i+1} {times_brasileirao[i]}")
    elif escolha == 3:
        print (f" os times em ordem alfabetica : ")
        listaTimeBrasileirao = list(times_brasileirao)
        listaTimeBrasileirao.sort()
        print(listaTimeBrasileirao)
    elif escolha == 4:

        index = times_brasileirao.index("Chapecoense")
        print (f" o time de chapecoense esta em {index + 1} posição")
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")