"""
Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.

B) Em que posição foi digitado o primeiro valor 3.

C) Quais foram os números pares.

"""
numeros = (int(input("Digite um valor: ")), int(input("Digite um valor: ")), int(input("Digite um valor: ")), int(input("Digite um valor: ")))

print(f"Você digitou os valores {numeros}")

print(f"O valor 9 apareceu {numeros.count(9)} vezes.")

if 3 in numeros:
    print(f"O primeiro valor 3 foi digitado na posição {numeros.index(3)+1}.")
else:
    print("O valor 3 não foi digitado.")

pares = []
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)

if len(pares) > 0:
    print(f"Os números pares digitados foram {pares}.")
else:
    print("Não foram digitados números pares.")