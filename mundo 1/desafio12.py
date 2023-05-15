salario = float(input("qual o salario do funcionario? "))
QualOAumento = float(input("quantos % sera o aumento do funcionario? "))
SalarioComAumento = ((salario*QualOAumento)/100)+salario
print('o salario atual do funcionario é igual a {} seu aumento sera de {}% oque resulta em um salario de {} '.format(salario, QualOAumento, SalarioComAumento))