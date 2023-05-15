"""
Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, 
mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

"""
soma = 0
totalsoma = 0
while True:
    n1 = int(input("digite um numero inteiro, de 1 a 998, digite 999 ou maior para encerrar"))
    if n1 >= 999:
        print (f"{soma} foram digitados e a soma entre eles é {totalsoma}")
        print("encerrando o progrma..")
        break
    elif n1 < 999:
        soma += 1
        totalsoma += n1
        print (f"{soma} foram digitados e a soma entre eles é {totalsoma}")

