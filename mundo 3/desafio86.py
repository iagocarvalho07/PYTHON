"""
Exercício Python 086: Crie um programa que declare uma matriz 
de dimensão 3×3 e preencha com valores lidos pelo teclado. 
No final, mostre a matriz na tela, com a formatação correta.
"""

matriz = [[0, 0, 0] for i in range(3)]

for i in range(3):
    for j in range(3):
        while True:
            try:
                matriz[i][j] = int(input(f'Digite um valor para [{i}, {j}]: '))
                break
            except ValueError:
                print('Digite apenas valores inteiros, por favor.')
        
print('-=' * 30)

for row in matriz:
    print(*[f'[{num:^5}]' for num in row], sep='')
    
print('-=' * 30)