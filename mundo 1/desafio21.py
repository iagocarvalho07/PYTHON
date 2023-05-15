#Exercício Python 22: Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas e minúsculas.
# Quantas letras ao todo (sem considerar espaços).
# Quantas letras tem o primeiro nome.

nome = str(input("digite seu nome"))
print('analisando seu nome...')
print('seu nome em MAIUSCULA É : {}'.format(nome.upper()))
print('seu nome em minusculos É : {}'.format(nome.lower()))
print('seu nome tem: {} letras'.format(nome.count()))
print('seu primeiro nome é {} e tem letras'.format(nome.split(1), nome.count()) )


