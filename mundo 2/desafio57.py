"""
Exercício Python 57: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. 
Caso esteja errado, peça a digitação novamente até ter um valor correto.

"""
while True:
    sexo = input("Qual seu sexo? Digite M para masculino ou F para feminino: ").upper()

    if sexo == "M" or sexo == "F":
        print(sexo)
        break
    else:
        print("Opção inválida. Digite M para masculino ou F para feminino.")
