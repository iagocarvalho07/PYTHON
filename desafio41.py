"""
Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia
o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:

– Até 9 anos: MIRIM

– Até 14 anos: INFANTIL

– Até 19 anos: JÚNIOR

– Até 25 anos: SÊNIOR

– Acima de 25 anos: MASTER
"""
import datetime
nasceu = int(input("qual o seu ano de nascimento? "))
anoAtual = datetime.datetime.now().year
idade = anoAtual - nasceu

if idade <= 9:
    print('o atleta tem {} anos'.format(idade))
    print('Classificação: MIRIM')
elif idade > 9 and  idade <= 14:
    print('o atleta tem {} anos'.format(idade))
    print('Classificação: INFANTIL')
elif idade > 14 and idade <= 19:
    print('o atleta tem {} anos'.format(idade))
    print('Classificação: Junior')
elif idade > 19 and idade <= 25:
    print('o atleta tem {} anos'.format(idade))
    print('Classificação: Senior')
elif idade > 25:
    print('o atleta tem {} anos'.format(idade))
    print('Classificação: Master')