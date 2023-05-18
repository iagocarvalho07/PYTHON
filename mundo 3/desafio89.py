"""
Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. 
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa
mostrar as notas de cada aluno individualmente.
"""

alunos_com_notas = []
while True:
    aluno_n1n2 = []
    aluno_n1n2.append(input("Digite o nome do aluno: ").upper())
    aluno_n1n2.append(float(input("Digite a primeira nota do aluno: ")))
    aluno_n1n2.append(float(input("Digite a segunda nota do aluno: ")))
    alunos_com_notas.append(aluno_n1n2[:])
    continuar = input("Deseja adicionar algo mais? [S/N] ").upper()
    if continuar == 'N':
        break

todas_as_notas = input("Gostaria de ver todas as notas? [S/N] ").upper()

if todas_as_notas == 'N':
    notas_individuais = input("Gostaria de ver a nota de algum aluno individualmente? [S/N] ").upper()
    if notas_individuais == 'N':
        print('Ok, então estaremos encerrando o programa.')
    else:
        qual_aluno = input("Gostaria de ver a nota de qual aluno: ").strip().upper()
        for aluno in alunos_com_notas:
            if aluno[0] == qual_aluno:
                media = (aluno[1] + aluno[2]) / 2
                print(f"O aluno {qual_aluno} possui a média {media}")
                break
        else:
            print(f"O aluno {qual_aluno} não foi encontrado.")
else:
    for aluno in alunos_com_notas:
        nome_aluno = aluno[0]
        media = (aluno[1] + aluno[2]) / 2
        print(f"O aluno {nome_aluno} possui a média {media}")