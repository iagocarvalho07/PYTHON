"""
Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar
mostrando no final quantos palpites foram necessários para vencer.

"""
from time import sleep
import random

print('vou pensanr em um numero entre 0 a 5, tente adivinhar')
while True:
    pcnun = random.randint(0,5)
    nun = int(input('em que numero eu pensei? '))
    print('PROCESSANDO....')
    sleep(0.3)
    if nun == pcnun:
        print('vc acertou parabens')
        break
    else:
        print('numero errado eu pensei em {}, tente mais uma vez kkkkk'.format(pcnun)) 