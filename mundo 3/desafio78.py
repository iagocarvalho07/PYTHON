"""
Exercício Python 078: Faça um programa que leia 5 valores numéricos
e guarde-os em uma lista. No final, mostre qual foi o maior e o menor
valor digitado e as suas respectivas posições na lista.


"""
valores = [int(input("Digite um valor: ")) for _ in range(5)]
print("Mínimo:", min(valores))
print("Máximo:", max(valores))
print("Índice do menor valor:", valores.index(min(valores)))
print("Índice do maior valor:", valores.index(max(valores)))
