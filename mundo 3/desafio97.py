"""
Exercício Python 097: Faça um programa que tenha uma função chamada escreva(), 
que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
Ex:escreva(‘Olá, Mundo!’) Saída:     ~~~~~~~~~   Olá, Mundo!   ~~~~~~~~~
"""

def escreva(text):
    print(f'{"~"*len(text)}')
    print(text)
    print(f'{"~"*len(text)}')


texto = str(input("Digite um texto a sua escolha: "))
escreva(texto)