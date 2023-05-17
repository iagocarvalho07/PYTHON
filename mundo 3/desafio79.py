"""
Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. 
Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, 
em ordem crescente.
"""

numeros = []

while True:
    valor = int(input('Digite um número (999 para sair): '))
    if valor == 999:
        break

    if valor in numeros:
        print('Valor duplicado! Não vou adicionar...')
    else:
        numeros.append(valor)
        print('Valor adicionado com sucesso...')
      
numeros.sort()

print(f'Os valores digitados foram: {numeros}')
