"""
Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para
a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos
anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então
o empréstimo será negado.

"""
from time import sleep


print('simule seu financiamento')
imovel = float(input('qual o valor do imovel que pretende adquirir: '))
salario = float(input('Qual é sua renda mensal :'))
financiarAnos = float(input('em quantos anos pretende financiar: '))
prestacao = imovel/(financiarAnos*12)
parcelaPossivel = salario*0.30

print('Analisando a possibilidade de conceção de credito...')
sleep(1)

if  prestacao > parcelaPossivel:
    print('infelizmente não e possivel o financiamento')
    print('o valor da parcela {:.2f} e maoir que o percentual de {}'.format(prestacao, parcelaPossivel))
elif prestacao < parcelaPossivel:
    print('e possivel o financiamento')
    print('o valor da parcela {:.2f} e menor que o percentual de {} disponivel para financiamentos'.format(prestacao, parcelaPossivel))