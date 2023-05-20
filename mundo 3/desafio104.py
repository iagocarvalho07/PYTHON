"""
Exercício Python 104: Crie um programa que tenha a função leiaInt()
que vai funcionar de forma semelhante a função input() do Python
só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)

"""

def leiaInt(msg):
    ok = True
    valor = 0
    while ok:
        n = str(input(msg))
        if n .isnumeric():
            print(f" voce digitou o numero {n} ")
            valor = int(n)
            ok = False
        else:
            print("Digite um numero valido: ")
    return valor



digiteInteiro = leiaInt("digite um numero inteiro: ")