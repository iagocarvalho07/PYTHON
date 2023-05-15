"""
Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, 
mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
"""
soma = 0
contador = 0
media = 0
maior = None
menor = None
numeros = []

print("Programa para saber a média e o maior número digitado")

while True:
    continuar = input("Gostaria de continuar digitando números? [S/N] ").upper()
    
    if continuar == "S":
        n = int(input("Digite um número inteiro: "))
        numeros.append(n)
        
        if maior is None or n > maior:
            maior = n
            
        if menor is None or n < menor:
            menor = n
    elif continuar == "N":
        if numeros:
            soma = sum(numeros)
            media = soma / len(numeros)
        
        print("Obrigado por utilizar o programa!")
        print(f"A média dos números inteiros digitados foi: {media}")
        
        if maior is not None:
            print(f"O maior número digitado foi: {maior}")
        
        if menor is not None:
            print(f"O menor número digitado foi: {menor}")
        
        break
    else:
        print("Opção inválida.")

  #  media = 




