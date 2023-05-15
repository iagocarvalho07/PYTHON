"""
Exercício Python 56: Desenvolva um programa que leia o nome, 
idade e sexo de 4 pessoas. No final do programa, mostre: 
a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
"""

nomeHomemMaisVelho = ""
idadeHomemMaisVelho = 0
somaIdades = 0
mulheresMenores20 = 0
numeroMulheres = 0

for pessoa in range(1,5):
    nome = input(f"Digite o nome da {pessoa}ª pessoa: ")
    idade = int(input(f"Digite a idade de {nome}: "))
    sexo = input(f"Digite o sexo de {nome} (M para masculino e F para feminino): ")
    
    somaIdades += idade
    
    if sexo == "M":
        if idade > idadeHomemMaisVelho:
            nomeHomemMaisVelho = nome
            idadeHomemMaisVelho = idade
    elif sexo == "F":
        numeroMulheres += 1
        if idade < 20:
            mulheresMenores20 += 1
    

mediaIdades = somaIdades / 4
print(f"A média de idade do grupo é {mediaIdades:.1f} anos.")
print(f"O homem mais velho é {nomeHomemMaisVelho} e tem {idadeHomemMaisVelho} anos.")
print(f"Há {mulheresMenores20} mulheres com menos de 20 anos.")