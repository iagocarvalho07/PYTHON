"""
Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, 
guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. 
No final, mostre: 
A) Quantas pessoas foram cadastradas 
B) A média de idade 
C) Uma lista com as mulheres 
D) Uma lista de pessoas com idade acima da média
"""
pessoas = []
mulheres = []
idades = []

while True:
    pessoa = {}
    pessoa['nome'] = input('Nome: ')
    pessoa['idade'] = int(input('Idade: '))
    pessoa['sexo'] = input('Sexo [M/F]: ')
    pessoas.append(pessoa)
    
    if pessoa['sexo'] == 'F':
        mulheres.append(pessoa.copy())
        
    idades.append(pessoa['idade'])
    
    continuar = input('Quer continuar? [S/N] ').upper()
    if continuar == 'N':
        break

print(f'Foram cadastradas {len(pessoas)} pessoas.')

media = sum(idades) / len(pessoas)
print(f'A média de idade é de {media:.2f} anos.')

print('As mulheres cadastradas foram:')
for mulher in mulheres:
    print(mulher['nome'])


acima_da_media = []
for pessoa in pessoas:
    if pessoa['idade'] > media:
        acima_da_media.append(pessoa['nome'])

if acima_da_media:
    print('As pessoas com idade acima da média foram:')
    for pessoa in acima_da_media:
        print(pessoa)
else:
    print('Não houve pessoas com idade acima da média.')
