"""
Exercício Python 101: Crie um programa que tenha uma função chamada voto() 
que vai receber como parâmetro o ano de nascimento de uma pessoa
retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
"""

def voto(nascimento):
    from datetime import date
    idade = date.today().year - nascimento
    if idade > 18:
        print("o voto e obrigatorios!! ")
    elif idade >= 16 and idade < 18  and idade > 65:
        print("o voto e opcional")
    elif idade < 16 :
        print("Ainda não esta em idade para votação")

while True :
    EmQueAno = int(input("digite o ano de seu nascimento: "))
    voto(EmQueAno)
