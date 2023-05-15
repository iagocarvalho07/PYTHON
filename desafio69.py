"""
Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas. 
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. 
No final, mostre:

A) quantas pessoas tem mais de 18 anos.

B) quantos homens foram cadastrados.

C) quantas mulheres tem menos de 20 anos.
"""
maiores18 = homens = mulheres20 = 0

while True:
    idade = int(input('Digite a idade: '))
    sexo = input('Digite o sexo [M/F]: ').strip().upper()[0]
    
    if idade > 18:
        maiores18 += 1
    
    if sexo == 'M':
        homens += 1
    elif idade < 20:
        mulheres20 += 1
    
    opcao = input('Deseja continuar? [S/N] ').strip().upper()[0]
    if opcao == 'N':
        break

print(f'Total de pessoas com mais de 18 anos: {maiores18}')
print(f'Total de homens cadastrados: {homens}')
print(f'Total de mulheres com menos de 20 anos: {mulheres20}')

    
