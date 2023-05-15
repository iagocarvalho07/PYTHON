"""
Exercício Python 39:
Faça um programa que leia o ano de nascimento de um jovem e informe
de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar
se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
"""
import datetime
nasceu =  int(input("qual o seu ano de nascimento? "))
AnoAtual = datetime.datetime.now().year
SuaIdade =  AnoAtual - nasceu

if SuaIdade == 18:
    print('se é a hora exata de se alistar')
elif SuaIdade > 18:
    print('já passou do tempo do alistamento')
    print('já passaram {} anos de seu alistamento'.format((SuaIdade -18)))
elif SuaIdade < 18:
    print('ainda não é a hora do seu alistamento')
    print('faltam {} anos de seu alistamento'.format((18 - SuaIdade)))


