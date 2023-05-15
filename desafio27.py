### Exercício Python 27: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
nome = str(input('digite seu nome completo: ')).lower().split()
print('seu primeiro nome é: {}'.format(nome[0]))
print('seu ultimo nome é: {}'.format(nome[-1]))

