"""

Exercício Python 66: Crie um programa que leia números inteiros pelo teclado. 
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).

"""
parada = 0 
cont = 0
soma = 0
while True:

    n1 = int(input("digite um numero inteiro: ou digite 999 para encerrar "))
    if n1 == 999:
        break
    cont += 1
    soma += n1
print (f"foram digitados {cont} numeros, e a soma entre eles é {soma}")