"""

Exercício Python 49: Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher
só que agora utilizando um laço for.

"""

tabuada = int(input("escolha um numero para ver sua tabuada: "))

for x in range(0,11):

    print ("{} x {} = {}".format(tabuada,x, (tabuada*x)))