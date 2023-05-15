"""

Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos)
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

"""
palavras = ('cachorro', 'gato', 'computador', 'caneta', 'mesa')
vogais = ('a', 'e', 'i', 'o', 'u')

for palavra in palavras:
    print(f'\nNa palavra {palavra.upper()} temos as vogais: ', end='')
    for letra in palavra:
        if letra in vogais:
            print(letra, end=' ')
