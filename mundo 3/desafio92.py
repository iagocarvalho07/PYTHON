"""
Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o 
(com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, 
o dicionário receberá também o ano de contratação e o salário. 
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
"""

import datetime
trabalhadores = dict()

while True:
    nome = str(input("digite o Nome: ou digite [sair] para encerrar o programa: "))
    if nome.lower() == "sair":
            break
    anoNascimento = int(input("digite o ano de nascimento: "))
    trabalhador = int(input("digite o numero da CTPS: "))
    idade = datetime.datetime.today().year - anoNascimento

    trabalhadores = {"nome":nome, "anoNascimento":anoNascimento, "CTPS": trabalhador, "idade":idade }

    if trabalhadores["CTPS"] != 0:
        Contratacao = int(input("digite o ano de contratação: "))
        salario = float(input("digite o salario do trabalhador: "))
        aposentadoria = Contratacao+30-datetime.datetime.today().year + idade
        print (aposentadoria)
        trabalhadores.update({"Contratado": Contratacao,})
        trabalhadores.update({"Salario": salario})
        trabalhadores.update({"Aposentadoria": aposentadoria})
        print(f'{trabalhadores["nome"]} nasceu em {trabalhadores["anoNascimento"]} com a CTPS de Numero {trabalhadores["CTPS"]} foi contratadp em {trabalhadores["Contratado"]} e se aposentara com {trabalhadores["Aposentadoria"]} ')
    else: 
        print(f'{trabalhadores["nome"]} nasceu em {trabalhadores["anoNascimento"]} com a CTPS de Numero {trabalhadores["CTPS"]} ')

