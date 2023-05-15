# Exercício Python 18: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math
angulo = float(input('Digite o angulo que vc deseja'))
seno = math.sin(math.radians(angulo))
coseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print('para o angulo de {:.2f} tem o seno de {:.2f} o coseno de {:.2f} e a tangente de {:.2F} '.format(angulo, seno, coseno, tangente))