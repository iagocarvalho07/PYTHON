"""

Exercício Python 090: Faça um programa que leia nome e média de um aluno, 
guardando também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

"""
students = []

for i in range(2):
    student = {}
    student["name"] = input("Digite o nome do aluno: ")
    student["average"] = float(input("Digite a media do aluno: "))
    if student["average"] >= 6:
        student["status"] = "Aprovado"
    else:
        student["status"] = "Reprovado"
    students.append(student)

for student in students:
    print(f'{student["name"]} teve média {student["average"]} e foi {student["status"]}')
