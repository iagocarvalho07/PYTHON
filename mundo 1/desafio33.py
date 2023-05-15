"""
Exercício Python 33:
, Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

"""


v1 = float(input('Digite o primeiro valor '))
v2 = float(input('Digite o segundo valor '))
v3 = float(input('Digite o terceiro valor '))
if v1 > v2 > v3:
    print(' {} é o maior valor'.format(v1))
elif v2 > v1 > v3:
        print(' {} é o maior valor'.format(v2))
elif v3 > v1 > v2:
     print(' {} é o maior valor'.format(v3))
if v1 < v2 < v3:
    print(' {} é o menor valor'.format(v1))
elif v2 < v1 < v3:
        print(' {} é o menor valor'.format(v2))
elif v3 < v1 < v2:
     print(' {} é o menor valor'.format(v3))
