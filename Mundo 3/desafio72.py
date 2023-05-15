"""
Exercício Python 72: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. 
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
"""




numeroExtenso =  ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    digiteAlgo = int(input("digite um numero entre 0 a 20 : "))
    if digiteAlgo > 20:
        print ("digite um numero valido")
        continue
    else:
        for i in range(0, len(numeroExtenso)):
            if i == digiteAlgo:
                print (f"o numero digitado foi {numeroExtenso[i]}")
    continuar = str(input(f"desaja continuar [S / N] ? ")).strip().upper()[0]
    if continuar == "S":
        continue
    elif continuar == "N":
        break
