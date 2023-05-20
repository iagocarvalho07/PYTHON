"""
Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias notas
de alunos e vai retornar um dicionário com as seguintes informações:
Quantidade de notas
a) A maior nota 
b) A menor nota
c) A média da turma                                                                                                                                                      
d) A situação (opcional)
"""

def notas(*notas, situacao=False):
    """
    -> Função para analisar notas e situação de vários alunos.
    :param notas: uma ou várias notas dos alunos (aceita valores decimais).
    :param situacao: valor opcional, indica se deve ou não adicionar a situação do aluno.
    :return: dicionário com várias informações sobre as notas da turma.
    """
    turma = {}
    
    turma['total'] = len(notas)
    turma['maior'] = max(notas)
    turma['menor'] = min(notas)
    turma['média'] = round(sum(notas) / len(notas), 2)
    
    if (not situacao):
        return turma
    
    if (turma['média'] >= 7):
        turma['situação'] = 'BOA'
    elif (turma['média'] >= 5):
        turma['situação'] = 'RAZOÁVEL'
    else:
        turma['situação'] = 'RUIM'
  
    return turma

    
