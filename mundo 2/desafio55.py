"""
Exercício Python 55: Faça um programa que leia o peso de cinco pessoas. 
No final, mostre qual foi o maior e o menor peso lidos.
"""

pesoMenor = 0
pesoMaior = 0
for x in range(1,6):
    MeDigaOPeso = float(input(f"Qual o peso da {x} pessoa: "))
    if pesoMaior < MeDigaOPeso:
        pesoMaior = MeDigaOPeso
    else:
        pesoMenor = MeDigaOPeso
print(f"o maior peso lido foi {pesoMaior} e o menor peso lido foi {pesoMenor}")