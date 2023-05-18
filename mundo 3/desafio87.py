"""
Exercício Python 087: Aprimore o desafio anterior, mostrando no final:                                                    
A) A soma de todos os valores pares digitados.             
B) A soma dos valores da terceira coluna.                                                                                                                
C) O maior valor da segunda linha.
"""

matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(3):
    for j in range(3):
        matrix[i][j] = int(input(f"Digite um valor para [{i},{j}]: "))

even_sum = 0
third_col_sum = 0
second_row_max = 0

for i in range(3):
    for j in range(3):
        if matrix[i][j] % 2 == 0:
            even_sum += matrix[i][j]
        if j == 2:
            third_col_sum += matrix[i][j]
        if i == 1 and matrix[i][j] > second_row_max:
            second_row_max = matrix[i][j]

print(f"Soma dos valores pares: {even_sum}")
print(f"Soma dos valores da terceira coluna: {third_col_sum}")
print(f"Maior valor da segunda linha: {second_row_max}")


