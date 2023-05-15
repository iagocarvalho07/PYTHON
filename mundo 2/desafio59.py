"""
Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:

[ 1 ] somar

[ 2 ] multiplicar

[ 3 ] maior

[ 4 ] novos números

[ 5 ] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.
"""
while True:
    n1 = float(input("digite um numero"))
    n2 = float(input("digite outro numero"))
    print("""
    Oque voce gostaria de fazer com os numeros digitados ?
[ 1 ] somar

[ 2 ] multiplicar

[ 3 ] maior

[ 4 ] novos números

[ 5 ] sair do programa
    """)
    escolha = int(input("me diga: oque pretende: "))
    if escolha == 1:
       soma = n1 + n2
       print(f"A soma é {soma}")
       break
    elif escolha == 2:
        multiplicar = n1 * n2
        print(f"A multiplicar {multiplicar}")
        break
    elif escolha == 3:
        maior = max(n1,n2)
    elif escolha == 4:
        continue
    elif escolha == 5:
        print(f"saindo do programa")
        break