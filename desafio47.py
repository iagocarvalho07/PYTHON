"""
Exercício Python 47: Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
"""
x = 1
for x in range(1, 50):
    if x % 2 == 0:
        print(x)
    x+=1