"""
Exercício Python 34: Escreva um programa que pergunte
o salário de um funcionário e calcule o valor do seu aumento.
para salários superiores a R$1250,00, calcule um aumentode 10%. 
Para os inferiores ou iguais, o aumento é de 15%
"""

funcionarios = float(input('Qual é o salario do funcionario? R$'))

if funcionarios > 1250:
    print ('funcionaros com salario superior a 1250 recebem aumento de 10%')
    print('seu salario passa a ser {:.2f}'.format((funcionarios*1.10)))
else:
    print ('funcionaros com salario inferior ou igual a 1250 recebem aumento de 15%')
    print('seu salario passa a ser {:.2f}'.format((funcionarios*1.15)))