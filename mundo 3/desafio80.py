"""
Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, 
já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
"""

numeros = []

for i in range(5):
    num = int(input('Digite um número: '))
    if i == 0:
        numeros.append(num)
        print('Número adicionado no final da lista.')
    else:
        posicao = 0
        for j in range(len(numeros)):
            if num > numeros[j]:
                posicao = j+1
            else:
                break
        numeros.insert(posicao, num)
        print(f'Número adicionado na posição {posicao} da lista.')
    
print('-'*30)
print(f'Lista ordenada: {numeros}')