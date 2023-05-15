"""
Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto, 
considerando o seu preço normal e condição de pagamento:

– à vista dinheiro/cheque: 10% de desconto

– à vista no cartão: 5% de desconto

– em até 2x no cartão: preço formal 

– 3x ou mais no cartão: 20% de juros
"""

produto = float(input("qual o preço do produto? "))

formaPagamento = float(input(
"""
1 - à vista dinheiro/cheque: 10% de desconto

2 -  à vista no cartão: 5% de desconto

3 -  em até 2x no cartão: preço formal 

4 -  3x ou mais no cartão: 20% de juros
Digite 1 , 2, 3 ou 4 para escolher a forma de pagamento:  """))

if formaPagamento == 1:
    print(' o preço do produto com 10% de desconto é igual a {}R$'.format((produto*0.9)))
elif formaPagamento == 2:
    print(' o preço do produto a vista no cartão com 5% de desconto é igual a {}R$'.format((produto*0.95)))
elif formaPagamento == 3:
    print(' o preço do produto em 2x no cartão correponde a {}R$ com parcelas de {}R$'.format(produto, (produto/2)))
elif formaPagamento == 4:
    print(' o preço do produto em 3x no cartão + 20% de juros correponde a {}R$ com parcelas de {}R$'.format((produto*1.20), ((produto*1.20)/2)))