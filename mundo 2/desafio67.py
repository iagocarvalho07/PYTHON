"""
Exercício Python 67: Faça um programa que mostre a tabuada de vários números, 
um de cada vez, para cada valor digitado pelo usuário. 
O programa será interrompido quando o número solicitado for negativo.

"""
while True:
    num = int(input('Digite um número para ver sua tabuada (digite um número negativo para sair): '))
    if num < 0:
        print('Programa encerrado.')
        break
    else:
        print(f'Tabuada do número {num}:')
        for i in range(1, 11):
            print(f'{num} x {i} = {num*i}')
