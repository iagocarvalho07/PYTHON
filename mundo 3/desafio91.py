"""
Exercício Python 091: Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. 
Guarde esses resultados em um dicionário em Python. No final, 
coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
"""
import random


jogadores = {}

for i in range(1, 5):
    resultado_dado = random.randint(1, 6)
    jogadores[f"Jogador {i}"] = resultado_dado

resultados = dict(sorted(jogadores.items(), key=lambda item: item[1], reverse=True))

for chave, valor in resultados.items():
    print(f"{chave} teve um resultado de {valor}")

vencedor = next(iter(resultados))
print(f"O vencedor é {vencedor} com um resultado de {resultados[vencedor]} no dado")
