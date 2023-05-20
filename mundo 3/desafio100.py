"""
Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). 
A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai 
mostrar a soma entre todos os valores pares sorteados pela função anterior.
Aula 
"""
from random import randint
from time import sleep

def sorteia(lista):
    print("os numeros gerados foram: ", end="")
    for item in range(0,5):
        n = randint(1,10)
        lista.append(n)
        print(f" {n} ", end="", flush=True)
        sleep(0.4)
    print("Pronto!!")
     


def somaPar(lista):
    soma = 0
    for item in lista:
        if item % 2 == 0:
            soma += item
    print(f" a soma dos numeros pares da lista {lista} é igual a {soma} ", end="", flush=True)
    sleep(0.4)



numero = list()
sorteia(numero)
somaPar(numero)