"""
Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os 
em uma lista única que mantenha separados os valores pares e ímpares. No final, 
mostre os valores pares e ímpares em ordem crescente.
"""

numericos = list()
par = list()
impar = list()
for item in range(0,7):

    numericos.append(int(input("digite um valor numerico: ")))

    if numericos[item] % 2 == 0:
        par.append(numericos[item])
        par.sort()
    elif numericos[item] % 2 == 1:
        impar.append(numericos[item])
        impar.sort()
        
listaUnica = [impar, par]
print(f" a lista impar tem o numeros {impar} a lista par tem o numeros {par}, e as duas listas {listaUnica}")