"""
Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos. 
O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

A) qual é o total gasto na compra.

B) quantos produtos custam mais de R$1000.

C) qual é o nome do produto mais barato.

"""
totalGasto = ProdutoMaior1000 = ProdutoMaisBarato = 0
nomeMaisBarato = None
while True:
    produto = str(input("qual o nome do produto: "))
    preco = int(input("qual o preço do produto: "))

    totalGasto += preco 

    if preco > 1000:
        ProdutoMaior1000 += 1
    
    if not ProdutoMaisBarato or preco < ProdutoMaisBarato:
        ProdutoMaisBarato = preco
        nomeMaisBarato= produto

    Continuar = input(f"deseja continuar [S/N ").strip().upper()[0]
    if Continuar == "S":
        continue
    elif Continuar == "N":
        print("obrigado pelas compras volte sempre, encerrando o progrma")
        break
    else : 
        print("opção invalida")

print(f'total gasto: {totalGasto}')
print(f' {ProdutoMaior1000} produtos custão mais de mil')
print(f' o produto mais barato é {nomeMaisBarato} que custa {ProdutoMaisBarato}')


