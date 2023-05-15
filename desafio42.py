"""
Exercício Python 42: Refaça o DESAFIO 35 dos triângulos,
acrescentando o recurso de mostrar que tipo de triângulo
será formado:

– EQUILÁTERO: todos os lados iguais

– ISÓSCELES: dois lados iguais, um diferente

– ESCALENO: todos os lados diferentes
"""
from time import sleep


print('Analisando triangulos')

r1 = float(input(" digite o comprimento da reta 1 : "))
r2 =  float(input(" digite o comprimento da reta 2 : "))
r3 = float(input(" digite o comprimento da reta 3 : "))

print('processando..')
import time

time.sleep(1)

r1 = float(input('Digite o valor de r1: '))
r2 = float(input('Digite o valor de r2: '))
r3 = float(input('Digite o valor de r3: '))

if r1 <= 0 or r2 <= 0 or r3 <= 0:
    print('Os valores devem ser positivos')
else:
 
    if r1 < r2 + r3 and r2 < r3 + r1 and r3 < r2 + r1:
        print('É um triângulo')
        if r1 == r2 and r2 == r3:
            print("É um triângulo equilátero")
        elif r1 != r2 and r2 != r3 and r3 != r1:
            print("É um triângulo escaleno")
        else:
            print("É um triângulo isósceles")
    else:
        print('Não é um triângulo')

