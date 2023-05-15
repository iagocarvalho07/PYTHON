"""
Exercício Python 35: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.


"""

from time import sleep


print('Analisando triangulos')

r1 = float(input(" digite o comprimento da reta 1 : "))
r2 =  float(input(" digite o comprimento da reta 2 : "))
r3 = float(input(" digite o comprimento da reta 3 : "))

print('processando..')
import time

time.sleep(1)

if r1 < r2 + r3 and r2 < r3 + r1 and r3 < r2 + r1:
    print('É um triângulo')
else:
    print('Não é um triângulo')

